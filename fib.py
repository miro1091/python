import time

input_list = [30, 13, 27, 15]

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

start = time.time() * 1000
for i in input_list:
    print(f(i))

print("Execution time", time.time() * 1000 - start)
