import sys
fastin = sys.stdin.readline

N, M = map(int, fastin().rstrip().split())
time = list(map(int, fastin().rstrip().split()))

start = max(time)
end = sum(time)
minvalue = end

while(start<=end):
    mid = (start+end)//2 # 블루레이의 크기
    minute = 0 # 블루레이 한 개에 들어갈 시간
    blu = M # 블루레이의 개수
    for i in range(N):
        if blu > 0:
            minute += time[i]
            if minute > mid:
                minute = time[i]
                blu -= 1
        elif blu < 1:
            break
    if blu > 1:
        end = mid - 1
    elif blu < 1:
        start = mid + 1
    else:
        minvalue = mid
        end = mid - 1

print(minvalue)