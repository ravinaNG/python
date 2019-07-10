n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
count = 0
duplicates_list = []
while(count < len(n)):
    counter = 1
    while(counter < len(n)):
        if(count == counter):
            break
        if(n[count] == n[counter]):
            duplicates_list.append(n[counter])
            n.pop(counter)
        counter = counter + 1
    count = count + 1
print (duplicates_list)
