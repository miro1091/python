import time

start_time = time.time()

from Queue import *
import threading

numbers = [999999, 999999, 999999, 999999]
q = PriorityQueue()
threads = []
queue_condition = threading.Condition()
shared_queue = Queue()

def fibonacci(condition, priority):
    with condition:

        while shared_queue.empty():
            condition.wait()

        num = shared_queue.get()
        a,b = 0,1
        for i in range(num):
            a,b = b,a+b
        q.put((priority, a))
    return

def queue_task(condition):
    with condition:
        for item in numbers:
            shared_queue.put(item)

        condition.notifyAll()

for i in range(4):
    t = threading.Thread(target = fibonacci, args = (queue_condition, i,))
    threads.append(t)

threads.append(threading.Thread(target=queue_task, args=(queue_condition,)));

for t in threads:
    t.start()

for t in threads:
    t.join()

while not q.empty():
    ans = q.get()
    q.task_done()
    print ans[1]

print("%s seconds" % (time.time() - start_time))