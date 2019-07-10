a = 0
b = 1
c = 0
print a, b,
while(c < 20):
	a = a + b
	b = b + a
	if (b>=100):
		break
	print a , b,
	c = c + 1
