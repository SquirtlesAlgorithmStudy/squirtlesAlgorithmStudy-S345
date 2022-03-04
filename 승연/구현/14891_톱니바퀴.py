from collections import deque

circle = [deque(map(int,input())) for _ in range(4)]
opers = deque(list(map(int,input().split())) for _ in range(int(input())))

while opers:
    num,direct = opers.popleft()
    num-=1 
    tmp_2 = circle[num][2]
    tmp_6 = circle[num][6]	
    circle[num].rotate(direct)
  
    tmp_direct=direct
    

    direct=tmp_direct
    for i in range(num-1,0-1,-1):
        if circle[i][2]!=tmp_6:		
          
            tmp_6=circle[i][6]
            circle[i].rotate(direct*-1)
            direct*=-1
        else:
            break

    direct=tmp_direct
    for i in range(num+1,4):
        if circle[i][6]!=tmp_2:		
          
            tmp_2 = circle[i][2]
            circle[i].rotate(direct*-1)
            direct*=-1
        else:
            break

ans=0
for i in range(4):
    if circle[i][0]==1:
        ans += (2**i)
print(ans)