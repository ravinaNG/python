string = str(raw_input("enter your string:- "))
caracter = str(raw_input("type one caracter which about you want to know:- "))
a = 0
b = 0
while (a < len(string)):
	if (caracter == string[a]):
		b = b + 1
	a = a + 1
print b
