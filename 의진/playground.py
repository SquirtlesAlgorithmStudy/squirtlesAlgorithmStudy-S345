<<<<<<< HEAD
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
=======
import sys
a = sys.stdin.readline().rstrip()

if a == '.':
    print("Yes")
else:
    print("No")
>>>>>>> 886fe739807e4b30c1e7978510aac5412fe119a8
