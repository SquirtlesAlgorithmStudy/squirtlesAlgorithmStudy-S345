import sys
fastin = sys.stdin.readline

#get : 가진 랜선 수
#need : 필요한 랜선 수
get, need = map(int, fastin().split())

#랜선 값 입력
lines = [ int(fastin()) for _ in range(get)]

start = 1
end = max(lines)

# 시작 값과 끝 값이 같을 때
while (start <= end):
  cnt = 0
  mid = (start + end) // 2
  
  for line in lines:
    cnt += line // mid
    
  if cnt >= need:
    start = mid + 1
    continue
    
  else:
    end = mid - 1
    continue
    
print(end)