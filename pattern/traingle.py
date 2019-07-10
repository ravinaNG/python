user = int(input("Type number:- "))
column = 0
while(column < user):
    row = 0
    while(row <= column):
        print ("*", end = "")
        row = row + 1
    print (" ")
    column = column + 1
