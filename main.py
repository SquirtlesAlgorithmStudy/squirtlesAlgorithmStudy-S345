import sys
fastin = sys.stdin.readline

n = 11

time = [[1,4],[3,5],[0,6],[5,7],[3,8],[5,9]
,[6,10],[8,11],[8,12],[2,13],[12,14]]
D = []
DS = []
c = 0 #횟수를 세는 함수
last = 0

time.append
for i in range(n):
  D.append(time[i][1]-time[i][0]) 
  DS = D.sort()
print(D)
print(DS)
time.sort(key=lambda x:(x[1],x[0]))

for i,j in time:
    if i>=last:
        c +=1
        last = j
print(c)


