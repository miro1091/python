import time

start_time = time.time()

from Queue import *
import threading

numbers = [999999, 999999, 999999, 999999]
q = PriorityQueue()
threads = []

def fibonacci(priority, num):

    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    q.put((priority, a))
    return
        

for i in range(4):
    t = threading.Thread(target = fibonacci, args = (i, numbers[i],))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

while not q.empty():
    ans = q.get()
    q.task_done()
    print ans[1]

print("%s seconds" % (time.time() - start_time))