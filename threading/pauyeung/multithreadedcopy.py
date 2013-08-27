import Queue
import threading
import shutil
import glob

fileQ = Queue.Queue()
src = './src'
dest = './dest'
fcnt = 0
total = 0

def Copy():
    while True:
        filename = fileQ.get()
        fileQ.task_done()
        shutil.copy(filename, dest)
        fcnt += 1
        print 'copied: ', fcnt, ' of ', total

def multithreadedCopy(filelist):
    total = len(filelist)
    for i in range(total):
        t = threading.Thread(target=Copy)
        t.daemon = True
        t.start()
    for file in filelist:
        fileQ.put(file)
    fileQ.join()

def main():
    cnt = 0
    filelist = glob.glob(src + '/' + '*.py')
    multithreadedCopy(filelist)

if __name__ == '__main__':
    main()
