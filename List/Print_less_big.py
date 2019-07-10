number = [50, 40, 23, 70, 56, 12, 5, 10, 7]
length = len(number)
i = 0
sum = 0
num = 0
while(i < length):
	if(number[i] > 20 and number[i] < 40):
		num = number[i]
		sum = sum + 1
	i = i + 1
print "Number who are <20 and >40 :-",num
print "How much number <20 and >40 :-",sum	
