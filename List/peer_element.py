num_list = [3, 5, 9, 0, 2, 3, 6, 2, 2, 5,7,9,7,9]
count = 0
sum = 0
while (count < len(num_list)):
    counter = count + 1
    while (counter < len(num_list)):
        if(num_list[count] == num_list[counter]):
            sum = sum + 1
            num_list.pop(counter)
            num_list.remove(num_list[count])
            count = -1
            break
        counter = counter + 1
    count = count + 1
print (sum)