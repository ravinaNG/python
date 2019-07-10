student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 011]
print student_marks
list_length = len(student_marks)
print "This is length of the List:- ", list_length
index = 0
less_than50 = 0
more_than50 = 0
while index < list_length:
	marks = student_marks[index]
	if marks < 50:
		less_than50 = less_than50 + 1
	else:
		more_than50 = more_than50 + 1
	index = index + 1
print "Marks more than 50: " + str(more_than50)
print "Marks less than 50: " + str(less_than50)
