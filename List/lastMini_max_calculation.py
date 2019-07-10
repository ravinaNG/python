num_list = [1,32, 100, 23, 46, 19, 90, 12, 23, 95, 100]
calculation = 0
counter = 0
max_num = 0
mini_num = 0
while (counter < len(num_list)):
    calculation += num_list[counter]
    if(num_list[counter] > max_num):
        max_num = num_list[counter]
    elif(num_list[counter] < max_num):
        mini_num = num_list[counter]
    counter += 1
print 'sum of elements :- ', calculation
print "maximum number of the list :- ", max_num
print "last and less then maximum number of the list :- ", mini_num