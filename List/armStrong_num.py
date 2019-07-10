# user = int(input("Enter your number which you want to chack:- "))
# num_list = list(str(user))
# sum = 0
# count = 0
# while(count < len(num_list)):
#     num = int(num_list[count])
#     number = num * num * num
#     sum = sum + number
#     print (num, " * ", num, " * ", num, " = ", number)
#     count = count + 1
# print ("Totle:- ", sum)
# print ("Your number:- ", user)
# if(sum == user):
#     print ("This is Armstrong number.")
# else:
    # print ("This is not Armstrong number.")



first = 0
last = 1000
while(first < last):
    num_list = list(str(first))
    sum = 0
    count = 0
    while(count < len(num_list)):
        num = int(num_list[count])
        number = num * num * num
        sum = sum + number
        # print (num, " * ", num, " * ", num, " = ", number)
        count = count + 1
    # print ("Totle:- ", sum)
    # print ("Your number:- ", user)
    if(sum == first):
        print ("This is Armstrong number:- ", first)
    # else:
    #     print ("This is not Armstrong number.")
    first = first + 1

