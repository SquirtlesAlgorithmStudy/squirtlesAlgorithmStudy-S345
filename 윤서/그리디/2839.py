# 설탕배달 - 큰 단위가 작은 단위의 배수가 아닌 경우
# 3kg, 5kg

sugar = int(input())    #배달할 설탕
deliver = 0             #배달할 봉지 수

while sugar > 0 :
    if sugar % 5 == 0:      # 5의 배수인 경우
        deliver += sugar // 5 
        sugar %= 5
    else :                  # 5의 배수가 아닌 경우 3kg 봉지를 사용한다. 5의 배수만큼의 kg가 남을 때 까지 반복 후 5kg을 사용
        sugar = sugar - 3
        deliver += 1

if sugar != 0 :
    print(-1)
else :
    print(deliver)