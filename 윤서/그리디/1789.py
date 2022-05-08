# 1789 - 수 들의 합

# 입력한 수
n = int(input())
sum = 0 
i = 1

while (n >= sum) :      # sum이 입력한 수보다 작거나 같은 경우
    sum += i            # i만큼 더해줌

    if sum <= n :        # 더한 결과 sum이 입력 수보다 작거나 같으면
        i += 1          # i 증가
        continue        # 반복문 재실행
    else :
        i -= 1          # sum이 입력한 수보다 커지면 i 하나 감소
        break
print(i)