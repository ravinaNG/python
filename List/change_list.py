a = [32, 23, 46, 19, 90, 12, 23, 95, 100, 1]
i = 0
l = len(a)
while (i < l/2):
    a[i] = a[l/2-i]
    i = i + 1
print a