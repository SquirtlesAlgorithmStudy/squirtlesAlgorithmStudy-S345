import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = [0] * N
for i in range(N):
    T[i] = int(input().rstrip())

start = 1
end = max(T) * M

minvalue = end

while(start <= end):
    mid = (start+end) // 2
    friend = 0
    for i in range(N):
        friend += mid // T[i]
    if friend >= M:
        minvalue = mid
        end = mid - 1
    else:
        start = mid + 1

print(minvalue)