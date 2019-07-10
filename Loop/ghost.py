list_a = [[1,0,3,4],
	      [2,1,0,3],
		  [0,0,1,0]]
sum = 0
count = 0
while(count < len(list_a)):
	counter = 0
	while (counter < len(list_a)):
		if list_a[counter][count] == 0:
			counter = counter + 1
		elif list_a[counter][count] == 0 or list_a[counter+1][count] == 0 :
			counter = counter + 1
		else:
			sum = sum + list_a[counter][count] 
		counter = counter + 1
	count = count + 1
print sum
		
