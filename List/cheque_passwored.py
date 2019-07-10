user = raw_input("Enter your passwored please:- ")
length = len(user)
a = 0
s = 0
b = 0
c = 0
if (length >= 6 and length <= 16):
	while (a < length):
		if(user[a] == "$"):
			s = s + 1 
		elif(user[a] == "2" or user[a] == "8"):
			b = b + 1 
		elif(user[a] == "A" or user[a] == "Z"):
			c = c + 1 
		a = a + 1
	if(s > 0 and b > 0 and c > 0):
		print "This is corect passwored."
	else:
		print "This is not corect passwored."


	
