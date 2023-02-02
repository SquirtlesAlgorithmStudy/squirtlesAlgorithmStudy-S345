import sys 
input = sys.stdin.readline
n,m = map(int,input().split())

battleground = [[]*m for _ in range(n) ]
visited = [[[0]*m for _ in range(n) ]]

battleground = [c [st = map(str,input().rstrip()) for b in battleground]for c in st ]

for b in battleground:
    st = map(str,input().rstrip())
    for c in st:
        b.append(c)
print(battleground)
