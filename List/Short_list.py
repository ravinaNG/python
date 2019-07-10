string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Humble", "Humble"]
m = len(string_list)
print "This is the length of string_list:- ", m
b = 0
c = 0
n = 0
while (b < m):
	while (c < b):
		if (string_list[b] == string_list[c]):
			sum = string_list[b]
			print sum,
		c = c + 1
	b = b + 1
