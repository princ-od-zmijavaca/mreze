# threading_primjer.py

import threading
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


try:
    threading._start_new_thread(print_time, ("Thread-1", 2,))
    threading._start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Threads not running")

while 1:
    pass
