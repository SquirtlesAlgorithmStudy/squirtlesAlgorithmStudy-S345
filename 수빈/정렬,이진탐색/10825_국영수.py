import sys
fastin = sys.stdin.readline

n = int(fastin())
a = []
score = []

## 시도1 = 정답은 맞으나 시간초과
for i in range(n):
    a = fastin().rstrip().split()
    score.append(a)

j = 0
while True:
    for i in range(n-1): 
        if int(score[i][1]) < int(score[i+1][1]):
            score[i], score[i+1] = score[i+1], score[i]
            i +=1
        else:
            i +=1
    j +=1
    print('국어점수 큰 순 정렬', j)
    if j==n:
        break

j = 0
while True:
    for i in range(n-1):
        if int(score[i][1]) == int(score[i+1][1]):
            print('영어점수 순으로 재정렬 시작')
            if int(score[i][2]) > int(score[i+1][2]):
                score[i], score[i+1] = score[i+1], score[i]
                i +=1
            else:
                i +=1
        else:
            i +=1
    j +=1
    print('영어점수 작은 순 정렬',j)
    if j==n:
        break
    
j = 0
while True:
    for i in range(n-1):
        if (int(score[i][1]) == int(score[i+1][1])) and (int(score[i][2]) == int(score[i+1][2])):
            print('수학점수 순으로 재정렬 시작')
            if int(score[i][3]) < int(score[i+1][3]):
                score[i], score[i+1] = score[i+1], score[i]
                i +=1
            else:
                i +=1
        else:
            i +=1
    j +=1
    print('수학점수 큰 순 정렬',j)
    if j==n:
        break
    
j = 0
while True:
    for i in range(n-1):
        if (int(score[i][1]) == int(score[i+1][1])) and (int(score[i][2]) == int(score[i+1][2])) and (int(score[i][3]) == int(score[i+1][3])):
            print('이름 순으로 재정렬 시작')
            if (score[i][0])>(score[i+1][0]):
                score[i], score[i+1] = score[i+1], score[i]
                i +=1
            else:
                i +=1
        else:
            i +=1
    j +=1
    print('이름 작은 순 정렬',j)
    if j==n:
        break
            

# print(score[0][0])

for x in score:
    print(x[0])


## 시도2 - sort와 lambda, - 를 사용해 짧게 코딩

import sys
fastin = sys.stdin.readline

n = int(fastin())
# list자체를 입력받는 것도 위에 append보다 더 짧게 한줄로 가능
score = [list(fastin().split()) for _ in range(n)]

score.sort(key=lambda x:( -int(x[1]), int(x[2]), -int(x[3]), x[0] ))


for x in range(n):
    print(score[x][0])


종류벌로 어떤 게 더 효율적인지 CS 면접 문제로 나왔던 적이 있음
문제가 어렵다기 보다는 개념이 중요한
그래서 백준으로 공부하는 것보다 이론을 공부하는 게 더 필요할수도

//
이 정렬방법은 어떤 특성의 데이터를 가지고 있을 때 빠르게 정렬을 먹는지
생각하는게 중요!
방법에 따라서, 같은 시간복잡도를 가지더라도, 데이터가 어떤 형태로 들어오느냐에 따라
완전히 정렬이 하나도 안되있는 형태로 들어오는 경우랑, 어느정도 정렬은 되어있고 1~2개만 바꾸면 되는 경우

1~2개만 바꾸면 되는 정렬방법인데, 전체를 다 탐색하는걸로 알고리즘으로 가면 비효율적이니까