#!/usr/bin/python

import Queue
import threading
import requests
import time

def worker():
    while True:
        item = q.get()
        print "\nI'm a worker thread, Puttin' in work!\n"
        print(item)
        start = time.time()
        try:
            r = requests.get('http://'+item, timeout=10)
        except:
            r = 'FAIL'
            print 'FAIL'
            pass
        end = time.time()
        loadtime = end - start
        if r != 'FAIL':
            print r.status_code
            print loadtime
            status_dict[item] = loadtime
        q.task_done()

num_worker_threads = 100
status_dict = {}

#Open URL File and build urllist while stripping out trailing \n's
with open('urlfile.txt') as f:
    urls = [line.rstrip() for line in f]

print urls
q = Queue.Queue()

for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

for item in urls:
    q.put(item)

q.join()    
print status_dict

for item in status_dict:
    print item, status_dict[item]
