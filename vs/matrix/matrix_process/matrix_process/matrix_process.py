
from multiprocessing import Process
import time
from queue import *

x1 = []
x2 = []
x3 = []
n = 999999

result = [0] * 3
for i in range(3):
    result[i] = [0] * n

for x in range(n):
  x1.append(x)
  x2.append(n-x)
  x3.append(2*n-x)

x = [x1, x2, x3]
y = [x3, x2, x1]

queue = PriorityQueue()
processes = []

def row(priority, n):

    for i in range(3):
        result[n][i] = x[n][0] * y[0][i] + x[n][1] * y[1][i] + x[n][2] * y[2][i]

    queue.put(priority, result)


if __name__ == '__main__':

    for i in range(3):
        processes.append(Process(target=row, args=(i, i,)))

    start = time.time()

    for p in processes:
            p.start()

    for p in processes:
            p.join()

    print("Execution time", time.time() - start)

    #results = []
    #for i in range(3):
        #results.append(queue.get()[i])

    #print(results[0][0])