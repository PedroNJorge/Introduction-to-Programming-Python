def collatz(n):
    seq = str(n) + ", "
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        seq += str(n) + ", "
    
    return seq[:-2]

# n = int(input())
# print(collatz(n))
