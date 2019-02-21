from multiprocessing import Process, Queue, Condition
import time

def fibonacci_task(condition, shared_queue, fibo_dict):
    with condition:

        while shared_queue.empty():
            condition.wait()

        value = shared_queue.get()
        a = 0
        b = 1
        for item in range(value):
            a, b = b, a + b
        fibo_dict.put(a)

def queue_task(condition, shared_queue, input_list):
    with condition:
        for item in input_list:
            shared_queue.put(item)

        condition.notify_all()


condition = Condition()
shared_queue = Queue()
fibo_dict = Queue()

p1 = Process(target=fibonacci_task, args=(condition, shared_queue, fibo_dict))
p2 = Process(target=fibonacci_task, args=(condition, shared_queue, fibo_dict))
p3 = Process(target=fibonacci_task, args=(condition, shared_queue, fibo_dict))
p4 = Process(target=fibonacci_task, args=(condition, shared_queue, fibo_dict))
queueP = Process(target=queue_task, args=(condition, shared_queue, [3, 10, 5, 7]))

start = time.time() * 1000

p1.start()
p2.start()
p3.start()
p4.start()
queueP.start()

p1.join()
p2.join()
p3.join()
p4.join()

print("Execution time", time.time() * 1000 - start)

results = []
for i in range(4):
    results.append(fibo_dict.get())

print(results)