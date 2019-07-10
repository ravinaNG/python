list1 = [3,5,1,4,2,6,7,9]
i = 0
new = []
while (i < len(list1)):
    min = list1[0]
    j = 0
    while (j < len(list1)):
        if (list1[j] < min):
            num = j
            min = list1[j]
        j = j + 1
    if (min == list1[0]):
        num = 0
    new.append(min)
    list1.remove(list1[num])
print (new)