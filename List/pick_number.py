list = [0, 1, 3, 2, 6, 5]
mid = 0
start = 0
end = len(list)
n = len(list)-1
while(start<end):
    if(list[0]>list[1]):
        print (list[0])
        # break
    elif(list[n]>list[n-1]):
        print (list[n])
        # break
    else:
        midPlus = mid
        mid = end//2
        mid2 = end-(mid+midPlus)
        if(mid-1 == -1 and mid2+1 == end):
            print ("There is no pick number. :)")
            break
        if(list[mid-1] <list[mid]> list[mid+1]):
            print (list[mid])
            # break
        if(list[mid2-1]<list[mid2]>list[mid2+1]):
            print (list[mid2])
            # break
    start = start + 1
