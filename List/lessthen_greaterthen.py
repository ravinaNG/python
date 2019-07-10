NUMBER = [50, 40, 23, 70, 56, 12, 5, 10, 7]
length_of_number = len(NUMBER)
i = 0 
sum = 0 
while (i < length_of_number):
	if(NUMBER[i] > 20 and NUMBER[i] < 40):
		print NUMBER[i]
		sum = sum + 1
	i = i + 1
print "Calculation of those number who are <20 and >40:- ", sum
