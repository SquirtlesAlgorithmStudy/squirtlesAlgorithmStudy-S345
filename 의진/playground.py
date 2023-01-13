import copy
a = [1, 2, [3, 4], 5, 6]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a[0] = 100000000
print(a)
print(b)
print(c)
print(d)

a[2][1] = 200000000
print(a)
print(b)
print(c)
print(d)