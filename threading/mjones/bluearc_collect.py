#!/usr/bin/python2.7
'''A script for gathering BlueArc NFS shares mounted on servers. It takes one
mandatory parameter, the BlueArc site location (either LAXHQ or SEA), and one
optional paramater, how many threads to use. Results are returned in
CSV format.
'''

import argparse
import MySQLdb
import paramiko
from Queue import Queue
from threading import Thread


class BlueArcServer(object):
    '''A connection to a server, with methods available to search/parse
    for an associated BlueArc NFS mount
    '''

    def __init__(self, server):
        '''Open the SSH connection'''
        self.server = server
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.server, username='root', timeout=20)

    def get_fstab(self):
        '''Parse fstab entries'''
        self.parsed = []
        stdin, stdout, stderr = self.ssh.exec_command("cat /etc/fstab |sed '/^#.*/d'")
        for line in stdout.readlines():
            if 'nfs' in line:
                self.parsed.append(line)
        return self.parsed

    def get_mounts(self, site):
        '''Collect Site-specific BlueArc mounts'''
        self.site = site
        if self.site  == 'sea':
            barcname = 'barcnfs'
        elif self.site == 'laxhq':
            barcname = 'tbarc'
        else:
            print "Invalid site name passed: %s" % self.site
            return False
        self.nfslist = self.get_fstab()
        self.mounts = []
        for line in self.nfslist:
            if barcname in line:
                line = line.split()
                nfs = line[0]
                mount = line[1]
                output = "%s %s:%s" % (nfs, self.server, mount)
                self.mounts.append(output)
        return self.mounts

    def disconnect(self):
        '''Disconnect ssh'''
        self.ssh.close()


def generate_queue():
    '''Generates our queue with all non-retired servers from RT'''
    dbconn = MySQLdb.connect(host='nops-infra02.shopzilla.com', user='rt_user', passwd='rt_pass', db='rt3')
    cur = dbconn.cursor()
    sql = "SELECT Name FROM AT_Assets WHERE Status != 'Retired' AND Type = '1' ORDER BY Name"
    cur.execute(sql)
    results = cur.fetchall()
    dbconn.close()
    dbqueue = Queue()
    for row in results:
        hostname = row[0]
        dbqueue.put(hostname)
    return dbqueue

def worker(i, queue, site):
    '''Thread working function, uses BlueArcServer() to perform lookups
    on hosts pulled from a populated Queue()
    '''
    while True:
        try:
            global currentcount
            global barcdict
            currentcount += 1
            name = queue.get()
            print "Trying %s (%d of %d)" % (name, currentcount, totalcount)
            server = BlueArcServer(name)
            mounts = server.get_mounts(site)
            for line in mounts:
                line = line.split()
                barcfs = line[0]
                mounted = line[1]
                if barcfs in barcdict:
                    barcdict[barcfs] = barcdict[barcfs] + ', ' + mounted
                else:
                    barcdict[barcfs] = mounted
            server.disconnect()
            queue.task_done()
        except Exception, err:
            errorstr = "Error with %s: %s\n" % (name, err)
            print errorstr
            queue.task_done()

if __name__ == "__main__":
    '''The master process that builds our host queue, spawns our worker threads,
    and handles thread feedback and CSV creation.
    '''
    barcdict = {}
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=str, help="BlueArc site (sea, laxhq) to collect for")
    parser.add_argument("-t", "--threads", type=int, help="Number of threads to use", default=20)
    parser.add_argument("-f", "--filename", type=str, help="File with hostnames to scan")
    args = parser.parse_args()
    # Assign values
    site = args.site
    filename = args.filename
    threads = args.threads
    currentcount = 0
    outputfile = open('bluearc_collect.csv', 'w')
    # Build our queue
    if filename:
        queue = Queue()
        for hostname in open(filename, 'r').readlines():
            queue.put(hostname.strip())
    else:
        queue = generate_queue()
    totalcount = queue.qsize()
    # Create our threads
    for i in range(threads):
       thread = Thread(target=worker, args=(i, queue, site)) 
       thread.setDaemon(True)
       thread.start()
    # Wait for completion
    queue.join()
    # Output to our CSV
    for nfs, mounts in barcdict.iteritems():
        writestr = "%s -- %s\n" % (nfs, mounts)
        outputfile.write(writestr)
    outputfile.close()
    print "Completed!"
