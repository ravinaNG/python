user = int(input("Enter number:- "))
count = 0
space = ""
column = user/2+1
while(count < column):
    num = 1
    row = 0
    space1 = 1
    while(row < user):
        if(space1 == 1):
            print (space, end = "")
            space1 = 0
        print ((num),end = "")
        if (num == 1):
            num = 0
        elif (num == 0):
            num = 1
        row = row + 1
    print ("")
    space1 = 1
    count = count + 1
    user = user - 2
    space = space + " "