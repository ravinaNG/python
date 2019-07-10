def function_print_lines():
	input = raw_input("What is your name:- ")
	input2 = raw_input("What you are doing:- ")
	print input
	print input2

function_print_lines()

def add_numbers(number1, number2):
	sum = number1 + number2
	print "<< Of Integer >>"
	print "Addition of both numbers :- ", sum
	print "-------------------------------------"

add_numbers(56, 12)

def add_numbers_list(list1, list2):
	length = len(list1)
	a = 0
	add = 0
	print "<< Element of List >>"  
	while (a < length):
		add = list1[a] + list2[a]
		print "Addition of both elements :- ", add
		print "---------------------------------------"
		a = a + 1
add_numbers_list([20, 30, 10, 12], [12, 23, 90, 0])

	
	
