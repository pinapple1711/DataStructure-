#fiboncci is a sequence of numbers that the later one is the sum of the two befor it
#1 1 2 3 5 8 13 ....
#we can do it By recursive and iterative
import time

def fib(n):
    
    if n < 3:
        return 1
    else:
       return fib(n-1) + fib(n-2)
    

def fib_iter(n):
    i1 = 0
    i2 = 1
    for i in range(0,n):
        i1,i2 = i2,i1+i2
    return i1   
#chack if the functions are working
print(fib(10),fib_iter(10))

for n in range(10, 41, 10):
    start_time = time.time()
    fib(7)
    print(f"Recursive for n={n}: {time.time() - start_time:.5f} seconds")

    start_time = time.time()
    fib_iter(7)
    print(f"Iterative for n={n}: {time.time() - start_time:.5f} seconds")

