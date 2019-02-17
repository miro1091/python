import time

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

start = time.time() * 1000

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

print("Execution time: ", time.time() * 1000 - start)
print(result)