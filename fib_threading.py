import threading
import queue
import time

fibo_dict = {}
shared_queue = queue.Queue()
input_list = [3, 10, 5, 7]

queue_condition = threading.Condition()


def fibonacci_task(condition):
    with condition:

        while shared_queue.empty():
            condition.wait()

        else:
            value = shared_queue.get()
            a, b = 0, 1
            for item in range(value):
                a, b = b, a + b
                fibo_dict[value] = a

        shared_queue.task_done()


def queue_task(condition):
    with condition:
        for item in input_list:
            shared_queue.put(item)

        condition.notifyAll()


thread1 = threading.Thread(target=fibonacci_task, args=(queue_condition,))
thread1.daemon = True

thread2 = threading.Thread(target=fibonacci_task, args=(queue_condition,))
thread2.daemon = True

thread3 = threading.Thread(target=fibonacci_task, args=(queue_condition,))
thread3.daemon = True

thread4 = threading.Thread(target=fibonacci_task, args=(queue_condition,))
thread4.daemon = True

queueThread = threading.Thread(name='queue_task_thread', target=queue_task, args=(queue_condition,))
queueThread.daemon = True

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