# 구글링한 코드입니다. 어렵당. ㅜㅜ

import sys
input = sys.stdin.readline

N= int(input())
timeTable = []

for i in range(N):
    timeTable.append(list(map(int,input().split())))

timeTable.sort()

meeting = timeTable[0]
meetingCnt = 1

for i in range(1, N):
    if meeting[0] < timeTable[i][0]:
        if meeting[1] <= timeTable[i][0]:
            meeting = timeTable[i]
            meetingCnt += 1
        elif meeting[1] >= timeTable[i][1]:
            meeting = timeTable[i]
    elif meeting[0] == meeting[1]:
        meeting = timeTable[i]
        meetingCnt += 1
        
print(meetingCnt)
