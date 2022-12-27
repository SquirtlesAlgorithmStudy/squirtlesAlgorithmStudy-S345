"""
strip() : 괄호 안에 있는 문자를 기준으로 쪼개서 저장
append(): 리스트 마지막에 요소 추가
"""

from sys import stdin
c=list(stdin.readline().rstrip().split('-')) 
## '-'를 읽으면 문자열을 쪼갬

s=[]

for i in c:
    sum=0
    tmp=i.split('+')
    for j in tmp:
        sum+=int(j)
    s.append(sum)

n=s[0]
for i in range(1,len(s)):
    n-=s[i]
print(n)
