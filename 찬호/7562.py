import sys 
from collections import deque
input = sys.stdin.readline

#number of test case 


n = int(input())

d = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
count = 0
min = 999999999999
def BFS(x,y,count):   
    if (x,y) == (dstx,dsty): #base condition
        if min > count:
            min =count
        return  
    queue = deque((x,y)) # put current position in the queue
    chssbrd[x][y] = 1 
    for dx,dy in d:
        nx = x+dx
        ny = y+dy
        if chssbrd(nx,ny) ==0 and 0< nx <l and 0<ny<l:
            queue.append((nx,ny))
            chssbrd[nx][ny] = 1
            BFS(nx,ny,count+1)
            
        else:
            pass 
        
while n: 

    l = int(input())
    
    chssbrd = [[0]*l for _ in range(l)] # as like visited list
    
    srtx,srty = map(int,input().split) # start point (tuple)
    dstx,dsty = map(int,input().split) # desti point (tuple)
    BFS(srtx,srty,0)

    
    