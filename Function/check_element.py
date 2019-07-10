def check_numbers(number1, number2):
	print " << Of integer >> "
	if(number1 % 2 == 0 and number2 % 2 == 0):
		print "Both numbers are even."
	else:
		print "Both numbers are not even."
	print "--------------------------------------"

check_numbers(12, 13)

def check_numbers_list(list1, list2):
	length = len(list1)
	a = 0
	print "<< Element of list >> "
	while (a < length):
		if(list1[a] % 2 == 0 and list2[a] % 2 == 0):
			print "Both numbers are even."
		else:
			print "Both numbers are not even."
		print "---------------------------------------"
		a = a + 1
check_numbers_list([2, 6, 18, 10, 3, 75], [6, 19, 24, 12, 3, 87])
