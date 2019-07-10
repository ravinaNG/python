user = input("Enter any String:- ")
if(len(user) == 1):
    print ("Empty.")
elif(len(user) == 2):
    user = user + user
    print (user)
else:
    count = 0
    l_f_list = ""
    while(count < len(user)):
        if(count == 0 or count == 1):
            l_f_list = l_f_list + user[count]
        elif(count == (len(user)-1) or count == (len(user)-2)):
            l_f_list = l_f_list + user[count]
        count = count + 1
    print(l_f_list)
