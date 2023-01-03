from sys import stdin
point=[[0]*100 for _ in range(100)]

num_of_colorpaper=int(input())

#색종이의 좌표 설정
for i in range(num_of_colorpaper):
    paper_x,paper_y=map(int,stdin.readline().rstrip().split())
    for j in range(paper_x,paper_x+10):
        for k in range(paper_y,paper_y+10):
            point[j][k]=1

#영역 넓이 계산
area=0
for x in range(100):
    for y in range(100):
        if point[x][y]==1:
            area+=1

print(area)