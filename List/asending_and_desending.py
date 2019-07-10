list = [9, 6, 8, 5, 7, 3, 4, 1, 2]
def max_num(list):
    i = 0
    max = list[0]
    while(i < len(list)):
        if(max < list[i]):
            max = list[i]
        i = i + 1
    return max
def remove_element(list, num):
    n = 0
    while (n < len(list)):
        if(list[n] == num):
            list.remove(num)
        n = n + 1

new = [9, 6, 8, 5, 7, 3, 4, 1, 2]
i = 0
s = -1
j = 0
k = 0
while(i < len(list)):
    max = max_num(list)
    if(k == 0):
        new[j] = max
        j = j + 1
        k = 1
        remove_element(list, max)
        i = 0
        continue
    if(k == 1):
        new[s] = max
        s = s - 1
        k = 0
        i = 0
        remove_element(list, max)
    # i = i + 1
print (new)
