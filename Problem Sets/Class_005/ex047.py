import math

PHI = (1 + math.sqrt(5)) / 2 
cache_fibo = {1: 1, 2: 1}


def fibo(n):
    if n not in cache_fibo.keys():
        cache_fibo[n] = fibo(n-1) + fibo(n-2)
    return cache_fibo[n]


def whichone(n):
    k = round(math.log((n)*(5**0.5), PHI)) - 3
    
    if n <= 3:
        return "ABA"[n - 1]
    else:
        while k > 3:
            if n > fibo(k-2) and n <= fibo(k-2) + fibo(k-3):
                k -= 3
                n -= 3
            else:
                k -= 2
                n -= 2
        print(n)
        return "ABA"[n - 1]

print(whichone(1))
print(whichone(2))
print(whichone(3))

print(whichone(4))
print(whichone(5))
print(whichone(10))
print(whichone(16))
