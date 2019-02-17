import threading
import time


values = []
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)

class Thread1(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starting " + self.name + "\n")

        n=int(input())
        global values
        values = [str(f(x)) for x in range(0, n+1)]

        print("End " + self.name + "\n")


class Thread2(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name



    def run(self):
        print("Starting " + self.name + "\n")
        print(values)
        print("End " + self.name + "\n")


thread1 = Thread1(1, "Thread 1")
thread2 = Thread2(2, "Thread 2")

thread1.start()
thread1.join()
thread2.start()
thread2.join()
# jeden thread caka, pokial neni zadanie vstupne cislo a az potom sa zacne vykonavat druhy