import sys
N = int(sys.stdin.readline())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA.sort()
listB.sort(reverse = True)
total = 0

for i in range(len(listA)):
    total += (listA[i] * listB[i])

print(total)