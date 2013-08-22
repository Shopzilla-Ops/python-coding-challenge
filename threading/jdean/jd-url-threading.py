#!/usr/bin/python

import Queue
import threading
import requests
import time

def worker():
    while True:
        item = q.get()
        #print "\nI'm a worker thread, Puttin' in work!\n",item
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
            print r.status_code,item,loadtime
            status_dict[item] = loadtime
            out_q.put([item,loadtime])
        q.task_done()

num_worker_threads = 10
status_dict = {}

#Open URL File and build urllist while stripping out trailing \n's
with open('urlfile.txt') as f:
    urls = [line.rstrip() for line in f]

print urls
q = Queue.Queue()
out_q = Queue.Queue()
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

for item in urls:
    q.put(item)

q.join()    

#iterate over an output queue. Must ensure its not empty.
while not out_q.empty():
    result = out_q.get()
    print result

for item in status_dict:
    print item, status_dict[item]
