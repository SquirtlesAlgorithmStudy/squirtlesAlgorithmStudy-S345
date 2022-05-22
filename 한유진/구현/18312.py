n, k = map(int, input().split())

count = 0
# k가 0인경우를 생각 못했다. 
# 시간이 한자리수일 경우에는 00시 00분 05초 이렇게 되어있으면 
for h in range(n + 1):
    if h < 10:
        hour = '0' + str(h)
    else:
        hour = str(h)
    for m in range(60):
        if m < 10:
            min = '0' + str(m)
        else:
            min = str(m)
        for s in range(60):
            if s < 10:
                sec = '0' + str(s)
            else:
                sec = str(s)
            time = hour + min + sec
            if time.count(str(k)):
                count += 1
print(count)