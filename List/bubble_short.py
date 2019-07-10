num_list = [-2, 45, 0, 11, -9]
count = 0
while(count < len(num_list)-1):
    if(num_list[count] > num_list[count + 1]):
        num_list[count], num_list[count +1] = num_list[count + 1], num_list[count]
    count = count + 1
    counter = 0
    while(counter < len(num_list) - 1):
        if(num_list[counter] > num_list[counter + 1]):
            num_list[counter], num_list[counter + 1] = num_list[counter+1], num_list[counter]
        counter = counter + 1
print ("Short list:- ", num_list)