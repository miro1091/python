import threading
import queue
import time

fibo_dict = []
shared_queue = queue.Queue()
input_list = [30, 13, 27, 15]

queue_condition = threading.Condition()


def queue_task(condition):
    with condition:
        for item in input_list:
            shared_queue.put(item)

        condition.notifyAll()

def fibonacci_task(condition):
    with condition:

        while shared_queue.empty():
            condition.wait()

        value = shared_queue.get()
        a = 0
        b = 1
        for item in range(value):
            a, b = b, a + b
        fibo_dict.append(a)


thread1 = threading.Thread(target=fibonacci_task, args=(queue_condition,))
thread2 = threading.Thread(target=fibonacci_task, args=(queue_condition,))
thread3 = threading.Thread(target=fibonacci_task, args=(queue_condition,))
thread4 = threading.Thread(target=fibonacci_task, args=(queue_condition,))
queueThread = threading.Thread(target=queue_task, args=(queue_condition,))

start = time.time() * 1000

thread1.start()
thread2.start()
thread3.start()
thread4.start()
queueThread.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print("Execution time", time.time() * 1000 - start)

print("Result", fibo_dict)