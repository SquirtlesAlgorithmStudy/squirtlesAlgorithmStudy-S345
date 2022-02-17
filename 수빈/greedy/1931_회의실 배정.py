# 시도1
import sys
fastin = sys.stdin.readline

# n = int(fastin.input())
# D = [] #시간차이 담는 변수

n = 11
time = [[1,4],[3,5],[0,6],[5,7],[3,8],[5,9]
,[6,10],[8,11],[8,12],[2,13],[12,14]]

D = [3,2,6,2,5,4,4,3,4,11,2]
end = 0 #회의 끝나는 시간
c = 0   #회의 개수 count

for i in range(n):
  D.append(time[i][1]-time[i][0])
  D.sort()
print(D)

for i in range(D[i]):
  print(i)


## sort 비교
time = [[1,4],[3,5],[0,6],[5,7],[3,8],[5,9]
,[6,10],[8,11],[8,12],[2,13],[12,14]]
time.sort(key=lambda x:(x[1],x[0]))
print(time)
print('----------------------')

time2 = [[1,4],[3,5],[0,6],[5,7],[3,8],[5,9]
,[6,10],[8,11],[8,12],[2,13],[12,14]]
time2.sort(key=lambda x:x[1])
print(time2)


##final code
import sys
fastin = sys.stdin.readline

n = int(fastin())

time = []
c = 0 #횟수를 세는 함수
last = 0

for i in range(n):
    start, end = map(int,fastin().split())
    time.append([start, end])
time.sort(key=lambda x:(x[1],x[0]))

for i,j in time:
    if i>=last:
        c +=1
        last = j
print(c)
