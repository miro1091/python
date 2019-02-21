from multiprocessing import Process, Queue
import time

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def row(queue, n):

    for i in range(3):
        result[n][i] = x[n][0] * y[0][i] + x[n][1] * y[1][i] + x[n][2] * y[2][i]

    queue.put(result)


queue = Queue()
processes = []

for i in range(3):
    processes.append(Process(target=row, args=(queue, i)))

start = time.time() * 1000

for i in range(3):
        processes[i].start()

for i in range(3):
        processes[i].join()

print("Execution time", time.time() * 1000 - start)

results = []
for i in range(3):
    results.append(queue.get()[i])

print(results)