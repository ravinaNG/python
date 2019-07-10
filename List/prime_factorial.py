user = int(input("Type any number:- "))
count = 1
while (count <= user):
	counter = 2
	num = 0
	while (counter < count):
		if(count % counter == 0 or count % 2 == 0):
			num = 1
			break
		counter = counter + 1
	else:
		if(num == 0):
			print (count)
	count = count + 1
