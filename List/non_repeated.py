list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
list3 = list1 + list2
length = len(list3)
new_list = []
checkA = 0
while(checkA < length):
    checkB = 1
    while(checkB < length):
        if(list3[checkA] == list3[checkB]):
            listA = list3[checkA]
        else:
            listA = list3[checkA]
        checkB = checkB + 1
    print listA,
    checkA = checkA + 1
