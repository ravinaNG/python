list = [2,4,3,6,10,26,10,15,24,6,8,0,3,5]
count = 0
max_num = 0
ce_max_num = 0
while (count < len(list)):
    if list[count] > max_num:
        max_num = list[count]
    count = count + 1
count = 0
while count < len(list):
    if list[count] > ce_max_num and list[count] < max_num:
        ce_max_num = list[count]
    count = count + 1
print ce_max_num
