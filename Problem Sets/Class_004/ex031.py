def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


def combination(n, k):
    if k > n:
        return "NA"
    return factorial(n) // (factorial(k) * factorial(n-k))
