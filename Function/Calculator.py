def Calculator(number_x, number_y, operation):
	if operation == "add":
		number = number_x + number_y
	elif operation == "subtract":
		number = number_x - number_y
	elif operation == "multiple":
		number = number_x * number_y
	elif operation == "divide":
		number = number_x / number_y
	else:
		"You dont want to do anything."
	return number

number_1 = Calculator(24, 20, "add")
print "Addition of 24 and 20:- ", number_1
print "-------------------------------------"
number_2 = Calculator(50, 60, "multiple")
print "multiple of 50 and 60:- ", number_2
print "-------------------------------------"
number_3 = Calculator(80, 120, "divide")
print "divide of 80 and 120:- ", number_3
print "-------------------------------------"
number_4 = Calculator(90, 23, "subtract")
print "subtract of 90 and 23:- ", number_4
print "-------------------------------------"

print "<< By user input >>"
user1 = int(raw_input("Enter your first number:- "))
user2 = int(raw_input("Enter your second number:- "))
add_result = Calculator(user1, user2, "add")
print "This is addition of your numbers:- ", add_result
print "----------------------------------------------------"
subtract_result = Calculator(user1, user2, "subtract")
print "This is subtract of your numbers:- ", subtract_result
print "----------------------------------------------------"
multiple_result = Calculator(user1, user2, "multiple")
print "This is multiple of your numbers:- ", multiple_result
print "----------------------------------------------------"
divide_result = Calculator(user1, user2, "divide")
print "This is divides of your numbers:- ", divide_result
print "----------------------------------------------------"

