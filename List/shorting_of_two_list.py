list_a = [0, 5, 6, 8, 10]
list_b = [1, 2, 7, 9]
new = []
i = 0
j = 0
if(len(list_a) <= len(list_b)):
    while(j < len(list_b)):
        if((i == len(list_a) - 1) and i == j):
            if(list_a[i] < list_b[j]):
                new.append(list_a[i])
                new.append(list_b[j])
                i = i + 1
                j = j + 1
                continue
            else:
                new.append(list_b[j])
                new.append(list_a[i])
                i = i + 1
                j = j + 1
                continue
        if(i == len(list_a) - 1):
            new.append(list_b[j])
            j = j + 1
            continue
        if(list_a[i] < list_b[j]):
            new.append(list_a[i])
            i = i + 1
            continue
        if(list_a[i] > list_b[j]):
            new.append(list_b[j])
            j = j + 1
            continue
        if(list_a[i] == list_b[j]):
            new.append(list_a[i])
            new.append(list_b[j])
            i = i + 1
            j = j + 1
    print (new)
if(len(list_a) > len(list_b)):
    while(i < len(list_a)):
        if(j == len(list_b) - 1):
            new.append(list_a[i])
            i = i + 1
            continue
        if(list_a[i] < list_b[j]):
            new.append(list_a[i])
            i = i + 1
            continue
        if(list_a[i] > list_b[j]):
            new.append(list_b[j])
            j = j + 1
            continue
        if(list_a[i] == list_b[j]):
            new.append(list_a[i])
            new.append(list_b[j])
            i = i + 1
            j = j + 1
    print (new)