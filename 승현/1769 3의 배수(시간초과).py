 #각 자리수 더한 값
def first (n,cnt):
  re = 10**len(str(n)) # 10의 배수
  if int(n) % re < 10: #입력받은 값이 10보다 작을 경우
    if int(n) % 3 == 0:
      print(cnt)
      print ('YES')
    else:
      print(cnt)
      print('NO')
  # 입력받은 값이 10보다 클 경우
  elif int(n) % re >= 10:
    # 반복하면서 나누어 나온 몫을 더한다
    result = 0
    for i in str(n):
      result += int(i)
    cnt += 1
    return first(result,cnt)
    
# 값 입력
a = input()
cnt = 0
first(a,cnt)

#iterable : 반복할 수 있는