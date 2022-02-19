import sys
fastin = sys.stdin.readline

n = int(fastin())
confers = [tuple(map(int, fastin().rstrip().split())) for _ in range(n)]


def sortingrule(x):
    return (x[1], x[0])


confers.sort(key=sortingrule)
print(confers)

result = 1
last_time = confers[0][1]

for confer in confers[1:]:
    if confer[0] >= last_time:
        result += 1
        last_time = confer[1]

print(result)
