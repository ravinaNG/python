n = int(input("Type number:- "))
row = 1
column = n/2
while(row <= n):
    space = column
    while(space > 0):
        print (" ", end="")
        space = space - 1
    start = 1
    while(start <= row):
        print ("*", end="")
        start = start + 1
    print (" ")
    column = column - 1
    row = row + 2
row = row - 4
column = n/2
space = 1
while(space < column):
    space_s = 0
    while(space_s < space):
        print (" ", end = "")
        space_s = space_s - 1
    start = row
    while(start > 0):
        print ("*", end="")
        start = start -1
    print (" ")
    row = row - 2
    space = space + 1