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
  #but, 여기서 엑셀에 A,B,C해준 것처럼 별도의 index가 필요하고, 그 index를 지정해주고-불러오고 하는 과정에서 코드가 지나치가 불필요하고 복잡하게 길어졌음



##final code
import sys
fastin = sys.stdin.readline

n = int(fastin())

time = []
c = 0 #횟수를 세는 함수
last = 0

for i in range(n):  #회의의 개수만큼 반복
    start, end = map(int,fastin().split())
    time.append([start, end]) 
  #D를 따로 두지 않고, 시작시간과 마침시간을 각각 받음
time.sort(key=lambda x:(x[1],x[0]))
#마침시간을 기준을 정렬하고, 시작시간을 기준으로 다시 재정렬

for i,j in time:
    if i>=last:
        c +=1
        last = j
print(c)


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
#여기 예제입력만 본다면 x[1]만 해줘도 되긴 함
#하지만 예제로 주어지지 않은 모든 경우를 고려하고, 반례까지 생각해주기 위해서는 x[0]도 같이 해주는 것이 바람직함
#sort도 여러 가지 방법이 있었는데, 구글링하면서 이렇게 key에 lambda를 주고 바로 .sort를 하는 식이 가장 간단하고 한 줄로 처리할 수 있는거라 이 방법을 사용함


**interval schedule문제**
1. 이른 시작시간 : 모든 일을 다하려면 최소 몇 개의 회의실이 필요?
2. 이른 끝나는시간 : 1개의 회의실이 있는데 최대 몇 개의 일을 하는지?
(이번 문제 풀이 방법)
3. 가장 짧게 걸리는 일
4. 가장 길게 걸리는 일
