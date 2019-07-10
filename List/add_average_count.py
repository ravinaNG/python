elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
odd_count = 0
even_count = 0
totle_count = 0
odd_sum = 0
even_sum = 0
totle_sum = 0
odd_average = 0
even_average = 0
totle_average = 0
count = 0
while (count < len(elements)):
    totle_count = totle_count + 1
    totle_sum = totle_sum + elements[count]
    if(elements[count] % 2 != 0):
        odd_count = odd_count + 1
        odd_sum = odd_sum + elements[count]
    elif(elements[count] % 2 == 0):
        even_count = even_count + 1
        even_sum = even_sum + elements[count]
    count = count + 1

odd_average = int(odd_sum / odd_count)
even_average = int(even_sum / even_count)
totle_average = int(totle_sum / totle_count)

print ("count of odd numbers:- ", odd_count)
print ("count of even numbers:- ", even_count)
print ("count of totle numbers:- ", totle_count)
print ("sum of odd numbers:- ", odd_sum)
print ("sum of even numbers:- ", even_sum)
print ("sum of totle numbers:- ", totle_sum)
print ("average of odd numbers:- ", odd_average)
print ("average of even numbers:- ", even_average)
print ("average of totle numbers:- ", totle_average)
