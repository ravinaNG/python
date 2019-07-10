user = int(input("Enter any number:- "))
print (" ")
last = user * 2 - 1
count = 1
while (count <= last):
    if (count == 1 or count == user or count == last):
        print (user * "*")
    elif (count > user):
        print ((user - 1) * " ", end = "*")
        print ("")
    else:
        print ("*")
    count = count + 1