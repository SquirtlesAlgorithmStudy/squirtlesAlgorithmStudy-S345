import sys
fastin = sys.stdin.readline
N = int(fastin().rstrip())

arr = []
for i in range(N):    
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x:(x[0], x[1]), reverse = True)
#print (arr)

count = 1
limit = arr[0][0]
for i in range(N):
    j = arr[i]
    if j[1] <= limit:
        count += 1
        limit = j[0]
        continue

print (count)