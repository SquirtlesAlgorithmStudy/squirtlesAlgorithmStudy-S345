import sys 
input = sys.stdin.readline
n,m = map(int,input().split())

battleground = [[]*m for _ in range(n) ]
visited = [[[0]*m for _ in range(n) ]]


for b in battleground:
    st = map(str,input().rstrip())
    for c in st:
        b.append(c)
print(battleground)
