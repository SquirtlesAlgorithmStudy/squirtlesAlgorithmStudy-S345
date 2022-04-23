
import sys
input = sys.stdin.readline
##가로만 보고 2짜리 인지 1짜리 인지 판별한다
## 2짜리라면 그 경우의 수에 *2를 해준다

n = int(input())
cnt = 0

a = [1,2]
b = [2,1]
c = [2,2]

dp = [0]