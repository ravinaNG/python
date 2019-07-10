list = [5, 9, 2, 8, 0, 3]
short = []
count = 0
while (count < len(list)):
    counter = count + 1
    while(counter < len(list)):
        if(list[count] > list[counter]):
            count = counter
        counter = counter + 1
    short.append(list[count])
    list.remove(list[count])
    count = 0
print (short)