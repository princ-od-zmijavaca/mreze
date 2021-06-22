import queue
import threading
import time

exitFlag = 0
threadList = ["Jedan", "Dva", "Tri", "Cetri", "Pet"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Running thread " + self.name)
        process_data(self.name, self.q)
        print("Killing thread " + self.name)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s procesuira %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)


for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.run()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for word in threadList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()
print("Izlazim iz glavne niti")
