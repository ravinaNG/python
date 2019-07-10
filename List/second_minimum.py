num_list = [3, 9, -4, 8, 7, 5, 0,-1, -2, -7]
mini_num = num_list[0]
position = 1
second_mini_num = num_list[0]
while(position < len(num_list)):
    if(mini_num > num_list[position]):
	second_mini_num = mini_num
        mini_num = num_list[position]
    position = position + 1
print ("second minimum number- ", second_mini_num)
print ("minimum number- ",mini_num)
