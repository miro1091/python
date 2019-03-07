import time

from queue import *
from multiprocessing import Process

numbers = [23, 23, 23, 23]
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

        # TODO: define process implementation for fibonacci function, which is above
        
        processes.append(p)

    start_time = time.time()

    # TODO: start all processes async with proper 2 methods

    print("%s seconds" % (time.time() - start_time))
