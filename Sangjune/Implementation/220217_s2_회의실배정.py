import sys

finput = sys.stdin.readline
n = int(finput())
count = 0
lastTime = 0
Meeting = []

for i in range(n):
    Meeting.append(list(map(int, finput().split())))

Meeting = sorted(Meeting, key=lambda x: (x[1], x[0]))

for i in range(len(Meeting)):
    startTime, endTime = Meeting[i][0], Meeting[i][1]
    # print(str(startTime) + ' ' + str(endTime))
    if startTime >= lastTime:
        count += 1
        lastTime = endTime

print(count)