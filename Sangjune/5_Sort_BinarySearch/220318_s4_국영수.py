import sys

fin = sys.stdin.readline

N = int(fin())
d = {}

for _ in range(N):
    inputList = list(fin().rstrip().split())
    d[inputList[0]] = list(map(int, inputList[1:]))

sorted_dict = dict(sorted(d.items(), key = lambda item: (-item[1][0], item[1][1], -item[1][2], item[0])))

for key in sorted_dict.keys():
    print(key)

# note
# dictionary 관련 methods
