num_of_computer=int(input())
pair_of_computer=int(input())

connected_computer=[[]*(num_of_computer+1) for _ in range(num_of_computer+1)]

from sys import stdin
for i in range(pair_of_computer):
    a,b=map(int,stdin.readline().rstrip().split())
    connected_computer[a].append(b)
    connected_computer[b].append(a)

virus=[0]*(num_of_computer+1)

count=0
def dfs(start):
    global count
    virus[start]=1
    for i in connected_computer[start]:
        if virus[i]==0:
            dfs(i)
            count+=1

dfs(1)
print(count)
        