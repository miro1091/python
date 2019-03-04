import time

from queue import *
from multiprocessing import Process

numbers = [999999, 999999, 999999, 999999]
q = PriorityQueue()
processes = []

def fibonacci(priority, num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    q.put((priority, a))
    return

if __name__ == '__main__':

    for i in range(4):
        priority = i
        num = numbers[i]
        p = Process(target = fibonacci, args = (priority, num))
        processes.append(p)

    start_time = time.time()

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    while not q.empty():
        ans = q.get()
        q.task_done()
        print(ans[1])

    print("%s seconds" % (time.time() - start_time))
