import time
from numpy import sqrt

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
    #print(f"dla {n} jest {len(arr)} elementow")  

def third_function(n):
    if n < 2 : return
    arr = [2, 3, 5, 7]
    id = 2
    for i in range(12, n + 1, 6):
        prime_a = True
        prime_b = True
        if arr[id] <= int(sqrt(i+1)+1): id += 1
        for a in arr[:id:]:
            if (i-1)%a==0: 
                prime_a = False
            if (i+1)%a==0:
                prime_b = False
            if not prime_b and not prime_a: break
        if prime_a: arr.append(i-1)
        if prime_b: arr.append(i+1)
    #print(f"dla {n} jest {len(arr)} elementow")


if __name__ == "__main__":
    N = 10**6
    #print(f"first metod,\t {N} elements, \t time = {check_time(first_function,N)}")
    print(f"second metod,\t {N} elements, \t time = {check_time(second_function,N)}")
    print(f"third metod,\t {N} elements, \t time = {check_time(third_function,N)}")
    

