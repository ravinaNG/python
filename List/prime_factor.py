n = input("Number:- ")
n = int(n)
prime_factor = 2
while(prime_factor < n):
    num = 2
    while(num < prime_factor):
        if(prime_factor % num == 0):
            break
        num = num + 1
    if(num == prime_factor):
        if(n % prime_factor == 0):
            print (prime_factor)
    prime_factor = prime_factor + 1