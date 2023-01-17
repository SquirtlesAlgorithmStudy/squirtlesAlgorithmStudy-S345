N=int(input())

from sys import stdin
conference_time=[]
for _ in range(N):
    start_time,end_time=map(int,stdin.readline().rstrip().split())
    conference_time.append([start_time,end_time])
    
conference_time=sorted(conference_time,key=lambda x:(x[1],x[0]))

num_of_conference=0
last_end_time=0

for start,end in conference_time:
    if start>=last_end_time:
        num_of_conference+=1
        last_end_time=end

print(num_of_conference)