N=int(input())
chart=[]
for _ in range(N):
    chart.append(list(input().split()))

chart.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for chart in chart:
    print(chart[0])
    
    
"""
1.list.sort(key=labmda x:(정렬 대상))
2.sort 함수의 key에서 내림차순일 때는 '-'를 붙여주면 된다.
3.정렬할 때 점수를 인트형으로 바꾸어 주거나 
  입력받을 때 점수를 인트형으로 받으면 된다.
"""