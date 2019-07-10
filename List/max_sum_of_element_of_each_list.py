def max_element(list):
    i = 0
    max_elmnt = list[0]
    while(i < len(list)):
        if(max_elmnt < list[i]):
            max_elmnt = list[i]
        i = i + 1
    return max_elmnt

def sum_of_element(list):
    i = 0
    sum = 0
    while(i < len(list)):
        sum = sum + list[i]
        i = i + 1
    return sum

num_list = [1, -4, -2, 2, 3]
element = []
sum_of_element = []
new = []
i = 0
while(i < len(num_list)):
    new.append(num_list[0])
    j = i + 1
    while(j < len(num_list)):
        new.append(num_list[j])
        j = j + 1
    print (new)
    print (sum_of_element(new))
    sum = sum_of_element(new)
    length = len(new)
    element.append(length)
    sum_of_element.append(sum)
    new = []
    i = i + 1
max_num = max_element(sum_of_element)
i = 0
while (i < len(sum_of_element)):
    if max_num == sum_of_element[i]:
        break
    i = i + 1
print(max_num, end=" ")
print(element[i])
