from threading import *

if __name__ == "__main__":
    ordinary_lock = Lock()

    ordinary_lock.acquire()
    print("{0} exiting".format(current_thread().getName()))
    ordinary_lock.acquire()

    print("{0} exiting".format(current_thread().getName()))

    ordinary_lock.release()
    ordinary_lock.release()

