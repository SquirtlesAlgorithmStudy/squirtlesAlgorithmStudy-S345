import sys
input = sys.stdin.readline

N=int(input())

times=[tuple(map(int,input().rstrip().split())) for _ in range(N)]

times.sort(key=lambda x: (x[1],x[0]))

number=1
end_time=times[0][1]

for time in times[1:]:
    if time[0]>=end_time:
        number+=1
        end_time=time[1]

print(number)




