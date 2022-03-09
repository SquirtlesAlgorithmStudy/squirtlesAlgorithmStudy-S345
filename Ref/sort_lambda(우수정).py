# a = range(5)
# print(type(a))
# b = list(a)
# print(b)
# print(type(b))

# b = list(range(5))
# print(b)
# b.sort(reverse=True)
# print(b)

# c = list(range(5))
# print(c)
# d = sorted(c, reverse=True)
# print(c)
# print(d)

# e = list(reversed(c))
# print(e)
# print(c)


a = [(1, 2), (5, 2), (3, 4), (2, 4), (3, 6)]


def sortingRule(x):
    return (x[1], x[0])


b = sorted(a, key=sortingRule)
print(b)

b = sorted(a, key=lambda x: (x[0], x[1]))
print(b)
