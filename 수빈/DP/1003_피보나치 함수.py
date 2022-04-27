import sys
input = sys.stdin.readline

cnt0 = [1, 0]
cnt1 = [0, 1]

T = int(input())

for i in range(T):
    case = int(input())
    
    if case ==0:
        print("답 1 0")
    elif case ==1:
        print("답 0 1")
    else:
        for j in range(2, case+1):
            cnt0.append(cnt0[j-1] + cnt0[j-2])
            cnt1.append(cnt1[j-1] + cnt1[j-2])
        print("답",f"{cnt0.pop()} {cnt1.pop()}")
        cnt0 = [1,0]
        cnt1 = [0,1]