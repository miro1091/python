from multiprocessing import Process, Queue
import time

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def firstRow(name, queue):
    print('start', name)
    result[0][0] = x[0][0] * y[0][0] + x[0][1] * y[1][0] + x[0][2] * y[2][0]
    result[0][1] = x[0][0] * y[0][1] + x[0][1] * y[1][1] + x[0][2] * y[2][1]
    result[0][2] = x[0][0] * y[0][2] + x[0][1] * y[1][2] + x[0][2] * y[2][2]
    queue.put(result)
    print('end', name)

def secondRow(name, queue):
    print('start ', name)
    result[1][0] = x[1][0] * y[0][0] + x[1][1] * y[1][0] + x[1][2] * y[2][0]
    result[1][1] = x[1][0] * y[0][1] + x[1][1] * y[1][1] + x[1][2] * y[2][1]
    result[1][2] = x[1][0] * y[0][2] + x[1][1] * y[1][2] + x[1][2] * y[2][2]
    queue.put(result)
    print('end', name)

def thirdRow(name, queue):
    print('start', name)
    result[2][0] = x[2][0] * y[0][0] + x[2][1] * y[1][0] + x[2][2] * y[2][0]
    result[2][1] = x[2][0] * y[0][1] + x[2][1] * y[1][1] + x[2][2] * y[2][1]
    result[2][2] = x[2][0] * y[0][2] + x[2][1] * y[1][2] + x[2][2] * y[2][2]
    queue.put(result)
    print('end', name)

queue = Queue()
p1 = Process(target=firstRow, args=('row1', queue,))
p2 = Process(target=secondRow, args=('row2', queue,))
p3 = Process(target=thirdRow, args=('row3', queue,))

start = time.time() * 1000

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

print("Execution time", time.time() * 1000 - start)

result1 = queue.get()
result2 = queue.get()
result3 = queue.get()
finalResult = [result1[0], result2[1], result3[2]]

print(finalResult)