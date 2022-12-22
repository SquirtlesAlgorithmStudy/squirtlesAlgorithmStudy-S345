#물이 새는 파이프에 테이를 붙이는데 물이 새는 지점의 좌우 0.5씩은 간격을 주어야 함
#첫째 줄에 물이 새는 곳의 개수 N과 테이프의 길이 L이 주어진다. 
#둘째 줄에는 물이 새는 곳의 위치가 주어진다. N과 L은 1,000보다 작거나 같은 자연수이고, 물이 새는 곳의 위치는 1,000보다 작거나 같은 자연수이다.
#첫째 줄에 항승이가 필요한 테이프의 개수를 출력한다.

"""
<1>-2
4 2
1 2 100 101

<2>-2
4 3
1 2 3 4

<3>-3
3 1
3 2 1

=>기준점으로부터 다른 지점까지의 차+1이 테이프의 길이보다 작거나 같을 때까지 동작
  이후 다음 테이프 사용

"""
# 물이 새는 곳의 개수 N과 길이 L입력
N,L=map(int,input().split())

#물 새는 포인트 저장
point=list(map(int, input().split()))
point.sort(reverse=True)

#필요한 테이프의 길이와 개수 
needed_tape_num=0
point_start=0
point_finish=1

while(point_finish!=len(point)):
    if (point[point_start]-point_finish+1)>=L:
        needed_tape_num+=1
    elif (point[point_start]-point_finish+1)<L:
        point_finish+=1
    else:
        break
print(needed_tape_num)