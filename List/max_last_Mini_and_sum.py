a = [1,32, 100, 23, 46, 19, 90, 12, 23, 95]
l = len(a)
i = 0
s = 0
m1 = a[0]
m2 = a[0]
while (i < l):
    s += a[i]
    if a[i] > m1:
        m1 = a[i]
    if a[i] < m1:
        m2 = a[i]
    i = i + 1
print s, m1, m2