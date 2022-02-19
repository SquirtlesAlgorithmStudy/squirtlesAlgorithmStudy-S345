N = int(input())

start_end = []
end_list = []

for i in range(N):  # key : start 시간, value : end 시간
    sample_list = []
    start, end = input().split(" ")
    sample_list.append(int(start))
    sample_list.append(int(end))
    start_end.append(sample_list)

start_end.sort(key=lambda x: (x[1], x[0]))

for i in range(0, len(start_end)):  # value값만 담긴 리스트 생성
    end_list.append(start_end[i][1])

# end_list.sort()  # 회의 종료시간 기준으로 오름차순 정렬
count = 1
i = 0
j = 1
breaker = False

for _ in range(N):
    for _ in range(N):
        if (end_list[i] == start_end[j][0]) and (end_list[i] == end_list[j]):
            count += 1
            if j <= (len(end_list) - 2):
                i = j
                j = i + 1
                break
            else:
                breaker = True
                break
        elif end_list[i] <= start_end[j][0]:
            count += 1
            if j <= (len(end_list) - 2):
                i = j
                j = i + 1
                break
            else:
                breaker = True
                break
        else:
            if j <= (len(end_list) - 2):
                j += 1
            else:
                breaker == True
                break
    if breaker == True:
        break

print(count)