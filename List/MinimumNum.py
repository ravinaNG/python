numbers = [80,90,20,44,33,24,100,34,94]
print "The length:-",len(numbers)
position_of_number = 0
maximum_number = 0
minimum_number = maximum_number

while (position_of_number < len(numbers)):
	if (maximum_number < numbers[position_of_number]):
		maximum_number = numbers[position_of_number]
	if (minimum_number > numbers[position_of_number]):
		minimum_number = numbers[position_of_number]
	position_of_number+=1

print "This is the maximum number of the list:-",maximum_number
print "This is the minimum number of the list:-", minimum_number


