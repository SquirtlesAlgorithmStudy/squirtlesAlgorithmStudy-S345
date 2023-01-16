from sys import stdin

n = int(stdin.readline().rstrip())
list = stdin.readline().strip().split()
str = "".join(list)

one = str.split('2')
two = str.split('1')

one_idx = one.index(max(one))
two_idx = two.index(max(two))

one_fin = len(one[one_idx])
two_fin = len(two[two_idx])

print(max(one_fin, two_fin))