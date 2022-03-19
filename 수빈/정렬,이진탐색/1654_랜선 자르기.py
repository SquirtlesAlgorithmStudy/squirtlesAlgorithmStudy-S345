import sys
fastin = sys.stdin. readline

k, n = map(int, fastin().split())
leng = [ int(fastin()) for _ in range(k) ]
start , end = 1, max(leng)

while start <= end:
    mid = (start+end)//2
    cnt = 0 #랜선(leng)의 수
    for i in leng:
        cnt += i//mid   # 분할된 랜선의 수
        
    if cnt >=n:  #랜선 개수의 분기점
        start = mid +1
    else:
        end = mid -1
    


print(end)

# 이게 이진탐색 문제라는 것을 알고 풀었으니까 아이디어를 잡기 쉬운데
그걸 모르고 문제를 풀 경우 BFS/DFS랑 헷갈릴 수 있음
랜선의 길이가 작아지면 작아질수록 랜선을 나누기가 쉬우니까?
절반 지점을 잡았을 때 절반 지점의 랜선을 나눠줄 수 있다면
그 아래는 볼 필요가 없는 문제니까 > 이진탐색

특정 방향으로 갈 때 가능성이 높아지거나 낮아진다면
중간값을 정해서 그게 가능한지
가능하다면 한쪽을 버리면 되는
이런 구조의 문제일 때 >>> 이진탐색으로 풀면 됨

**이진탐색을 풀 때 중요한 건,
  중간값을 어떻게 잡을 것이냐