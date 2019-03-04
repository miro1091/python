import threading
import time
from Queue import *

x1 = []
x2 = []
x3 = []
n = 999999

for x in range(n):
  x1.append(x)
  x2.append(n-x)
  x3.append(2*n-x)

x = [x1, x2, x3]
y = [x3, x2, x1]

q = PriorityQueue()

def firstRow(priority):
    result = []
    temp = x[0][0] * y[0][0] + x[0][1] * y[1][0] + x[0][2] * y[2][0]
    result.append(temp)
    temp = x[0][0] * y[0][1] + x[0][1] * y[1][1] + x[0][2] * y[2][1]
    result.append(temp)
    temp = x[0][0] * y[0][2] + x[0][1] * y[1][2] + x[0][2] * y[2][2]
    result.append(temp)
    q.put((priority, result))

def secondRow(priority):
    result = []
    temp = x[1][0] * y[0][0] + x[1][1] * y[1][0] + x[1][2] * y[2][0]
    result.append(temp)
    temp = x[1][0] * y[0][1] + x[1][1] * y[1][1] + x[1][2] * y[2][1]
    result.append(temp)
    temp = x[1][0] * y[0][2] + x[1][1] * y[1][2] + x[1][2] * y[2][2]
    result.append(temp)
    q.put((priority, result))

def thirdRow(priority):
    result = []
    temp = x[2][0] * y[0][0] + x[2][1] * y[1][0] + x[2][2] * y[2][0]
    result.append(temp)
    temp = x[2][0] * y[0][1] + x[2][1] * y[1][1] + x[2][2] * y[2][1]
    result.append(temp)
    temp = x[2][0] * y[0][2] + x[2][1] * y[1][2] + x[2][2] * y[2][2]
    result.append(temp)
    q.put((priority, result))

thread1 = threading.Thread(target=firstRow, args=(0,))
thread2 = threading.Thread(target=secondRow, args=(1,))
thread3 = threading.Thread(target=thirdRow, args=(2, ))

start = time.time()

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Execution time", time.time() - start)

#while not q.empty():
 #   ans = q.get()
  #  q.task_done()
   # print ans[1]