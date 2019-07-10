List1 = [1, 342, 75, 23, 98]
List2 = [75, 23, 98, 12, 78, 10, 1]
m = len(List1)
n = len(List2)
a = 0
b = 0
c = 0
new_list = []
while (a < m):
	b = 0
	while (b < n):
		if (List1[a] == List2[b]):
			new_list.append(List1[a]) 
		b = b + 1
	a = a + 1
print new_list
