space = eval(input("Enter number:- "))
star = 1
while (space > 0):
    star_a = star
    space_a = space - 1
    while (space_a > 0):
        print ("")
        space_a = space_a - 1
    while (star_a > space_a):
        print ("*", end = ' ')
        star_a = star_a - 1
    space = space - 1
    star = star + 1
