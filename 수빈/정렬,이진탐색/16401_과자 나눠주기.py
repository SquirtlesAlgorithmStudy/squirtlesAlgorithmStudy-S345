import sys
fastin = sys.stdin.readline

m, n = map(int, fastin().split())
snack = fastin().split()
snack_int = list(map(int, snack))

snack = list(map(int, fastin().split())) ## 이렇게 한 줄로 쓸 수 있음

start, end = 1, max(snack_int)

while start<=end:
    mid = (start+end)//2
    cnt = 0  #막대 과자의 수
    if mid ==0:   # 이 문제 의도상 이 코드가 있어야 하지만, 어짜피 밑에 등호에서 걸리니까 있으나 없으나 상관없음
      break
    for i in snack_int:
        cnt += i//mid
    if cnt >= m:
        start = mid+1
    else:
        end = mid-1


print(end)

fastin 대신에 input으로 바꿔서 받아봤더니 시간이 많이 줄어들음
input으로 하면 이게 overwrite 되서 기존에 input은 쓸 수 없는

변수의 길이는 짧을수록 아주 쪼금 더 빨리 돌아가는 건 맞으나
크게 차이날 정도는 아니고, 가독성이 더 중요한 부분