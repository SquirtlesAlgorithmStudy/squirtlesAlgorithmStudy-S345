import sys 
input = sys.stdin.readlines

N = map(int,input())
M = map(int,input())


def DFS(visited,i,graph):
    

visited = [0 for _ in  range(N)]
computers = []
for i in range(M):
    [x,y] =map(tuple,input())
    computers.append([x,y])
    
