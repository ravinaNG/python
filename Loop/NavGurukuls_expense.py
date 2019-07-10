num_of_student = int(raw_input("How much student are in the NavGurukulo. :- "))

expense_one_student = int(raw_input("How much of one student cost? :- "))

Total_expense = num_of_student * expense_one_student
print "Our total expense is :- ", Total_expense
if (Total_expense < 50000):
	print "Wow! We are under of the budget."
else:
	print "Our expense is out of budget."
