# # idea 1 (x)
# 강의 리스트를 다합해서 M으로 나누기 (i라 하자.)
# 여기서 이분탐색을 어떻게 적용할 수있을까 ?
# 오름차순으로 정렬 된 강의 길이 list
# mid값을 기준으로 처음부터 mid값까지 sum
# -> i 값이랑 비교해서 i값보다 작으면 오른쪽 탐색 / 크면 왼쪽 탐색
# 즉, i값이랑 가장 비슷한 값 찾기

# idea 2 (o)
# 블루레이의 최대 길이 : 리스트의 합
# 최소 길이 : 리스트의 최댓값
# 만약 리스트에 1~9가 저장돼 있다면 최소, 최대 길이는 각각 9, 45
# 이때 블루레이에 들어갈 수 있는 레슨은 1개, 9개
# start, end 설정해주고, start와 end에 포함된 리스트 합이 mid보다 커지면 블루레이 개수 1 증가
# 위와 같은 방법으로 얻은 블루레이 수가 M보다 작으면 end 줄여주고, M보다 크다면 start 늘려주기

n, m = map(int, input().split())
courses = list(map(int, input().split()))
start, end = max(courses), sum(courses)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    temp = 0
    for i in range(n):
        if temp + courses[i] > mid:
            cnt += 1
            temp = 0
        temp += courses[i]

    # temp가 0이 아니면 cnt += 1
    cnt += 1 if temp else 0

    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)