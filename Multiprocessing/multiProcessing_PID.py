import multiprocessing
import os

def worker1():
    print("Process of worker1 running: {}".format(os.getpid()))

def worker2():
    print("Process of worker2 running: {}".format(os.getpid()))

if __name__ == "__main__":
    print("main process ID: {}".format(os.getpid()))
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("worker 1 ID: {}".format(p1.pid))
    print("worker 2 ID: {}".format(p2.pid))

    print("worker 1 is alive? {}".format(p1.is_alive()))
    print("worker 2 is alive? {}".format(p2.is_alive()))
