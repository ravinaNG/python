# num_list = [-2, 45, 0, 11, -9]
num_list = [-2, 45, 0, 11, 44, -33, -2, -9, -9]
new_l = []
count = 0
mini = 0
sec_mini = 0
while(count<len(num_list)):
    counter = 0
    while(counter < len(num_list)):
        if(num_list[counter] in new_l):
            if(counter + 1 != len(num_list) and num_list[counter + 1] not in new_l):
                mini = num_list[counter+1]
        elif(num_list[counter] < mini):
            mini = num_list[counter]
        counter = counter + 1
    if (mini not in new_l):
        new_l.append(mini)
    # sec_mini = mini
    mini = 0
    count = count + 1
print (new_l)
