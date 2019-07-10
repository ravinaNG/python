numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
print "This is lenght :-", (len(numbers))
position_of_numbers = 0
biger_then_numbers = 0

while position_of_numbers < len(numbers):
	if biger_then_numbers < numbers[position_of_numbers]:
		biger_then_numbers = numbers[position_of_numbers]
	position_of_numbers+=1

print "This is the bigest numbers of the list:-",biger_then_numbers





