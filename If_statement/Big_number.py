First = int(raw_input("Enter your first number:- "))
Second = int(raw_input("Enter your Second number:- "))
Third = int(raw_input("Enter your Third number:- "))
if(First > Second and First > Third):
	print "First number is your bigest number:- ", First
elif(Second > First and Second > Third):
	print "Second number is your bigest number:- ", Second
elif(Third > First and Third > Second):
	print "Third number is your bigest number:- ", Third
else:
	print "Here no any number is bigest number."
