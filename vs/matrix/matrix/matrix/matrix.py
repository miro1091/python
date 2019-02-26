import time

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

start = time.time()

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

#print(result)
print("Execution time: ", time.time() - start)

