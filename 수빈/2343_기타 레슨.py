# 시도1
from posixpath import split
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
gitar_class = list(map(int, input().split()))

start, end = max(gitar_class), sum(gitar_class)
cnt = 0 #블루레이의 수
hap_list = []

while cnt<=m:
    mid = end//2
    print('mid 감소',mid)
    cnt = 0  
    hap = 0
    for i in reversed(gitar_class):
        hap += i
        if hap<=mid:
            i +=1
            print('hap출력', hap)
            hap_list.append(hap)
        else:
            hap= 0 #합 초기화
            cnt +=1
            hap +=i
            print('합 초기화', cnt)
    cnt +=1
    end -=2
    

print('최종 mid', mid, '최종 cnt', cnt, '최종hap', hap)
print('최종 답', hap_list)

# 시도2 - 런타임 에러
import sys
from turtle import right
input = sys.stdin.readline

def add_lesson():
    cnt = 0 # 레코드 개수
    sum_lesson = 0  # 한 레코드에 들어갈 레슨들의 합
    for i in range(N):
        if sum_lesson + lesson_list[i] >mid:
            cnt +=1
            sum_lesson = 0
            
        sum_lesson += lesson_list[i]
    else:
        if sum_lesson:
            cnt +=1
    return cnt
        
        
if __name__=="__main__":
    N, M = map(int, input().split())
    lesson_list = list(map(int, input().split()))
    
    left, right = max(lesson_list), sum(lesson_list)
    
    while left<=right:
        mid = (left+right)//2
        cnt = add_lesson()
        
        if cnt<=M:
            right = mid-1
        else:
            left = mid +1
            
    print(left)

# 시도3 - 정답

from operator import le
from posixpath import split
import sys
from turtle import right
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    lesson_total = sum(arr)
    left, right = lesson_total//M, sum(arr)
    print('초기 right', right)
    
    answer = right
    while left <= right:
        mid = (left + right) // 2
        print('초기 mid', mid )

        if mid < max(arr):
            left = mid + 1
            continue
        # 조건 만족 확인
        count, temp = 0, 0
        for i in range(len(arr)):
            if arr[i] > mid:
                break
            elif temp + arr[i] <= mid:
                temp += arr[i]
                print('elif문의 temp', temp)
            else:
                temp = arr[i]
                count += 1
                print('else문의 temp', temp, 'count',count)

        if count <= M - 1:  # 가능한 경우 (더 작은 값이 있는지 확인해야 한다)
            right = mid - 1
            print('변경된 right', right)
            print('answer ', answer,'mid ', mid)
            answer = min(answer, mid)  # answer 값 업데이트
            print('변경된 answer', answer)
        else:  # 값을 증가시켜야 한다.
            left = mid + 1
            print('증가한 left ', left)

    print(answer)