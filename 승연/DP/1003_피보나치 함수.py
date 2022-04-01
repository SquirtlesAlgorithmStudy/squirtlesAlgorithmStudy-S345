#idea : 3일 때 0과 1의 개수를 각각 저장, 4일 때 0과 1의 개수를 각각 저장, .... -> 6의 0과 1의 개수를 구할 땐 4와 5의 0과 1의 개수를 더하면 된다.

import sys
input = sys.stdin.readline

testCase = int(input())
testList = []
for i in range(testCase):
    testList.append(int(input()))

#풀긴 풀었는데.... 찝찝하다.
for i in range(testCase):
    infoList = []
    infoList_0 = [0] * (testList[i] + 1)
    infoList_1 = [1] * (testList[i] + 1)
    if testList[i] == 0:
        print(1, 0)
    elif testList[i] == 1:
        print(0, 1)
    elif testList[i] == 2:
        print(1, 1)
    else:
        for j in range(3, testList[i] + 1):
            infoList_0[2] = 1
            infoList_0[j] = infoList_0[j - 1] + infoList_0[j - 2]
            infoList_1[j] = infoList_1[j - 1] + infoList_1[j - 2]
        print(infoList_0[testList[i]], infoList_1[testList[i]])