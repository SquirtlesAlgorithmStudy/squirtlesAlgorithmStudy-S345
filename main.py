from collections import deque

a = [deque(), deque()]

a[0].append(1)
a[0].append(2)
while a[0] or a[1]:
    a[0].pop()
