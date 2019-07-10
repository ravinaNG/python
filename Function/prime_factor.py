def prime_factor(user):
    prime_factor = 0
    i = 1
    while(i < user):
        j = 2
        while (j < i):
            if(i % j == 0):
                break
            j = j + 1
        if(i == j):
            if(user % i == 0):
                prime_factor = i
                j = 2
                print (prime_factor)
        i = i + 1
    return prime_factor

user = int(input("Enter any number:- "))
print (prime_factor(user))
