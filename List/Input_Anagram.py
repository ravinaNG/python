string1 = raw_input("Enter first string:- ")
string2 = raw_input("Enter second string:- ")
m = len(string1)
n = len(string2)
a = 0 
if(m == n):
	while(a < m):
		b = 0
		while(b < n):
			if(string1[a] == string2[b]):
				c = 0
				c = c + 1
			b = b + 1
		a = a + 1
	i = 0
	i = m % c 
	if (i % 2 == 0):
		print "This is Anagram."
	else:
		print "This is not a Anagram."
else:
	print "This is not a Anagram."
