#import numpy as np
import time

def check_time(fun, n):
    start = time.time()
    fun(n)
    return f"{time.time()-start} seconds"

def first_function(n):
    arr = []
    for i in range(2, n):
        not_prime = True
        for j in range(2, i):
            if i%j==0:
                not_prime = False
                break
        if not_prime: arr.append(i)
    
    #print(arr)


if __name__ == "__main__":
    N = 10**5
    print(f"first metod,\t {N} elements, \t time = {check_time(first_function,N)}")
    

