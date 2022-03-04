#1769 3의 배수
 #각 자리수 더한 값
def first (n,cnt):
  if len(n) < 2: #입력받은 값이 10보다 작을 경우
    if int(n) % 3 == 0:
      print(cnt)
      print ('YES')
    else:
      print(cnt)
      print('NO')
  # 입력받은 값이 10보다 클 경우
  else:
    result = 0
    
    for i in n:
      result += int(i)
    cnt += 1
    return first(str(result),cnt)
    
# 값 입력
a = input()
cnt = 0
first(a,cnt)

#iterable : 반복할 수 있는