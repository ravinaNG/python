list_a = [10,1,2,3,4,5]
count = 0
sum = 0
store = 0
while (count < len(list_a)):
    if list_a[count] > store or list_a[0]==0:
        store = list_a[count]
    elif list_a[count] <= store :
        sum = sum + 1
    count = count + 1
if sum > 1:
    print "False"
else:
    print "True"