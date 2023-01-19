from copy import deepcopy
N = int(input())
times =[]
chklist=[]
for i in range(N):
    a,b =input().split()
    times.append((a,b))  
times.sort(key=lambda x:x[0])
min = 4000000
st_point = 0
count = 0
for time in times:
    _check =deepcopy(chklist)
    start,end =time
    start=int(start);end=int(end)
    duration =end-start 
    if(st_point==start):
        if duration<min:
            for i in range(start,end+1):
                _check.append(count)
    else:
        count = count +1
        min =40000
        st_point = start
        chklist = deepcopy(_check)
        
print(count)
            
        
    
    
    