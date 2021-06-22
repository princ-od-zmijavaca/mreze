# threading_2.py

import threading
import time
import datetime

# from threading_primjer import print_time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Running thread " + self.name)
        print_time(self.name, 5, self.counter)
        print("Killing thread " + self.name)


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


t1 = myThread(1, "T1 ", 1)
t2 = myThread(2, "T2 ", 2)

t1.run()
t2.run()

print("Leaving main thread")
