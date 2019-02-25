import threading
import time
from Queue import *

x1 = []
x2 = []
x3 = []
xn = []
n = 999999

for x in range(n):
  x1.append(x)
  x2.append(n-x)
  x3.append(2*n-x)
  xn.append(0)

x = [x1, x2, x3]
y = [x3, x2, x1]
result = [xn, xn, xn]

def firstRow(name):
    print('start', name)
    result[0][0] = x[0][0] * y[0][0] + x[0][1] * y[1][0] + x[0][2] * y[2][0]
    result[0][1] = x[0][0] * y[0][1] + x[0][1] * y[1][1] + x[0][2] * y[2][1]
    result[0][2] = x[0][0] * y[0][2] + x[0][1] * y[1][2] + x[0][2] * y[2][2]
   
    print('end', name)

def secondRow(name):
    print('start ', name)
    result[1][0] = x[1][0] * y[0][0] + x[1][1] * y[1][0] + x[1][2] * y[2][0]
    result[1][1] = x[1][0] * y[0][1] + x[1][1] * y[1][1] + x[1][2] * y[2][1]
    result[1][2] = x[1][0] * y[0][2] + x[1][1] * y[1][2] + x[1][2] * y[2][2]
  
    print('end', name)

def thirdRow(name):
    print('start', name)
    result[2][0] = x[2][0] * y[0][0] + x[2][1] * y[1][0] + x[2][2] * y[2][0]
    result[2][1] = x[2][0] * y[0][1] + x[2][1] * y[1][1] + x[2][2] * y[2][1]
    result[2][2] = x[2][0] * y[0][2] + x[2][1] * y[1][2] + x[2][2] * y[2][2]
   
    print('end', name)

start = time.time()

thread1 = threading.Thread(target=firstRow, args=('row1',))
thread2 = threading.Thread(target=secondRow, args=('row2',))
thread3 = threading.Thread(target=thirdRow, args=('row3',))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Execution time", time.time() - start)

print(result[0][0])