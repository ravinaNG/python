array = [1, 7, 3, 8, 9, 2, 4]
index = 0
while (index < len(array)):
    count = 0
    while(count <= len(array)-2):
        if(count == len(array)-1):
            break
        if (array[count] > array[count+1]):
            sift = array[count]
            array[count] = array[count+1]
            array[count+1] = sift
        count = count + 1
    index = index + 1
print (array)