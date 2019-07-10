num = 6
sum = 0
count = 1
while (count < num):
    if(num % count == 0):
        print (count)
        sum = sum + count
    count = count + 1
print ("sum:- ",sum)
if(sum == num):
    print ("perfect.")
else:
    print ("nothing")

# first = 1
# last = 1000
# while (first < last):
#     num = first
#     sum = 0
#     count = 1
#     while (count < num):
#         if(num % count == 0):
#             # print (count)
#             sum = sum + count
#         count = count + 1
#     # print ("sum:- ",sum)
#     if(sum == num):
#         print (num)
#     # else:
#     #     print ("nothing")
#     first = first + 1