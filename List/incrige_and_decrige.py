count = 0
counter = 1
user = int(input("Enter your number:- "))
while(count <= user):
    print("*"*counter)
    if(count == user):
        number = user - 1
        num = 0
        counter = counter - 1
        while(num <= number):
            print("*"*counter)
            num = num + 1
            counter = counter - 1
    count = count + 1
    counter = counter + 1 