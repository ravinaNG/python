def list_change(list1, list2):
	length = len(list1)
	a = 0
	sum = 0
	while(a < length):
		b = list1[a] * list2[a]
		print b ,
		a = a + 1
	return b

multiple = list_change([5, 10, 50, 20], [2, 20, 3, 5])
print multiple
