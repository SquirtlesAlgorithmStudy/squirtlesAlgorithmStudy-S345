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
    blu = 1 # 사용한 블루레이의 개수
    for i in range(N):
        minute += time[i]
        if minute > mid:
            minute = time[i]
            blu += 1
    if blu <= M:
        end = mid - 1
        minvalue = mid
    else:
        start = mid + 1

print(minvalue)