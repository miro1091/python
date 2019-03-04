import time

start = time.time()

input_list = [999999, 999999, 999999, 999999]

def f(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a


for i in input_list:
    f(i)

print("Execution time(s)", time.time() - start)

