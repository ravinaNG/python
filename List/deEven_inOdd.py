num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
count = -1
print (-(len(num_list)-1))
while(count > -len(num_list)):
    if(num_list[count] % 2 == 0):
        new_list.append(num_list[count])
    if(count == -(len(num_list)-1)):
        num = 0
        while(num < len(num_list)):
            if(num_list[num] % 2 != 0 and num_list[num] != 1):
                new_list.append(num_list[num])
            num = num + 1
    count = count - 1
print (new_list)