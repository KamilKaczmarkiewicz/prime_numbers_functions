#import numpy as np
import time

from numpy import sqrt
from numpy import ceil

def check_time(fun, n):
    start = time.time()
    fun(n)
    return f"{time.time()-start} seconds"

def first_function(n):
    arr = []
    for i in range(2, n + 1):
        not_prime = True
        for j in range(2, i):
            if i%j==0:
                not_prime = False
                break
        if not_prime: arr.append(i)
    
    #print(arr)

def second_function(n):
    if n < 2 : return
    arr = [2, 3]
    for i in range(6, n + 1, 6):
        a = i - 1
        b = i + 1
        first_not_prime = True
        second_not_prime = True
        for j in range(2, int(sqrt(a))+1):
            if a%j==0:
                first_not_prime = False
                break        
        for j in range(2, int(sqrt(b))+1):
            if b%j==0:
                second_not_prime = False
                break
        if first_not_prime: arr.append(a)
        if second_not_prime: arr.append(b)
    
    #print(arr)


if __name__ == "__main__":
    N = 10**5
    print(f"first metod,\t {N} elements, \t time = {check_time(first_function,N)}")
    print(f"second metod,\t {N} elements, \t time = {check_time(second_function,N)}")
    

