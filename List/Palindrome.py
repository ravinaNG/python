string = raw_input("Type your string which you want to chaque:- ")
a = 0
b = -1
while (a < len(string)):
	if (string[a] == string[b]):
		s = "This is Palindrome."
	elif (string[a] != string[b]):
		s = "This is not a Palindrome String."
		break
	a = a + 1
	b = b - 1
print s















	
