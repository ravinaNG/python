big_list = ['2','4','5','3','6','5','3','6','8','7']
user = input("Enter a list:- ")
user = list(user)
print (user)
index = 0
user_index = 0
sum = 1
while (index < len(big_list)):
    if(user_index == len(user)):
        break
    if(big_list[index] == user[user_index]):
        index = index + 1
        user_index = user_index + 1
        while (user_index < len(user)):
            if(index == len(big_list)):
                print (False)
                break
            if(user[user_index] != big_list[index]):
                sum = 1
                index = index - 1
                user_index = 0
                break
            sum = sum + 1
            index = index + 1
            user_index = user_index + 1
        if(sum == len(user)):
            print (True)
            break
    index = index + 1
