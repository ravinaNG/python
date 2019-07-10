number_list = [6, 12, 17, 23, 38, 45, 77, 84, 90]
number = 45
first_index = 0
last_index = len(number_list)-1
mid_number= (last_index+first_index)/2
mid_index = int(mid_number)
print (type(mid_index))
while(first_index <= last_index):
    if(number == number_list[first_index]):
        print (True)
        break
    elif(number == number_list[last_index]):
        print (True)
        break 
    elif(number == number_list[mid_index]):
        print (True)
        break
    elif(number < number_list[mid_index]):
        last_index = mid_index
        mid_number = (last_index+first_index)/2
        mid_index = int(mid_number)
    elif(number > number_list[mid_index]):
        first_index = mid_index
        mid_number = (last_index+first_index)/2
        mid_index = int(mid_number)
    else:
        print (False)
