#뒤집게
#0과 1로만 이루어진 문자열에서 모든 숫자를 같게 만들 때
#연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것만 가능한 조건일 때
#최소 횟수?

"""
1.000|11|00(1)
경계 2개
->경계의 개수가 짝수인 경우, 경계/2회 뒤집기

2.11111(0)
경계 0개
->경계가 없는 경우, 뒤집지 않는다


3.0000000|1(1)
경계 1개
->경계의 개수가 홀수인 경우, (경계수+1)/2회 뒤집기

4.11|00|11|00|11|00|11|00000|1(4)
경계 8개
->경계의 개수가 짝수인 경우, 경계/2회 뒤집기

5.111|0|11|0|1(2)
경계 4개
->경계의 개수가 짝수인 경우, 경계/2회 뒤집기

6.0|1|00|1|0|11(3)
경계 5개
->경계의 개수가 홀수인 경우, (경계수+1)/2회 뒤집기

7.0|1|0|1|0|111|00|11(4)
경계 7개
->경계의 개수가 홀수인 경우, (경계수+1)/2회 뒤집기

<방법>
1.경계 수 세기
2.뒤집은 횟수 세기
3.뒤집은 횟수 출력
"""

#문자열 입력
s=input()
#경계 수 세기
boundary=0
num_reverse=0
for i in range(len(s)):
    if s[i]!=s[i-1]:
        boundary+=1  
#뒤집는 횟수 세기
    if boundary==0:
        num_reverse=0
    elif boundary%2==0:
        num_reverse=boundary/2
    elif boundary%2==1:
        num_reverse=(boundary+1)/2
print(int(num_reverse))