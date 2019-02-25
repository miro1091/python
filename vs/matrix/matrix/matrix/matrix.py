import time

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

start = time.time()

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

print(result[0][0])
print("Execution time: ", time.time() - start)

