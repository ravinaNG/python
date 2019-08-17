def numbers_greater_than_twenty(list):
    list1 = list
    counter = 0
    new_list=[]
    while counter < len(list1):
        item = list1[counter]
        if item > 20:
            list1.remove(item)
            counter=counter-1
        if item<20:
            new_list.append(item)
        counter=counter+1
    return new_list
num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
list3 = num_list
num_list_20 = numbers_greater_than_twenty(list3)
print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_20) 

