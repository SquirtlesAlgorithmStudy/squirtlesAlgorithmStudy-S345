"""
strip() : 괄호 안에 있는 문자를 기준으로 쪼개서 저장
append(): 리스트 마지막에 요소 추가
"""

from sys import stdin
c=list(stdin.readline().rstrip().split('-')) 
## '-'를 읽으면 문자열을 쪼갬

s=[]

for i in c: ## '-'를 기준으로 쪼개진 것에 대해
    sum=0
    tmp=i.split('+') ## '+'를 기준으로 또 쪼갬
    for j in tmp: ## 다시 쪼갠 것에 대해
        sum+=int(j) ## 숫자를 더함
    s.append(sum) ## 리스트의 마지막에 요소 추가

n=s[0] ## 기준이 될 첫 항
for i in range(1,len(s)):
    n-=s[i] ##최소가 되어야 하므로 빼줌
print(n)