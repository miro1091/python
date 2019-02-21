import time

input_list = [30, 13, 27, 15]

def f(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

start = time.time() * 1000
for i in input_list:
    print(f(i))

print("Execution time", time.time() * 1000 - start)
