def sum1(n):
    if (n==0):
        return 0
    return sum1(n-1) + n

print sum1(6)