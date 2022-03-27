import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

start = 1
end = sum(lectures)

while start <= end:
    mid = (start + end) // 2
    lecture_min = 0
    cnt = 0
    for lecture in lectures:
        if (lecture_min + lecture <= mid):
            lecture_min += lecture
        else:
            if (lecture > mid):
                cnt = m + 1
                break
            cnt += 1
            lecture_min = lecture
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)
