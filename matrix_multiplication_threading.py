import threading
import time

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


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

thread1 = threading.Thread(target=firstRow, args=('row1',))
thread2 = threading.Thread(target=secondRow, args=('row2',))
thread3 = threading.Thread(target=thirdRow, args=('row3',))

start = time.time() * 1000

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Execution time", time.time() * 1000 - start)

print(result)