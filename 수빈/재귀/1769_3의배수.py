import sys
fastin = sys.stdin.readline

def func(Y, cnt):
    if len(Y) >1:
        cnt +=1
        t=0
        for i in Y:
            t +=int(i)
            # print(t)
        func(str(t), cnt)
    else:
        if int(Y) %3 ==0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")
   
n = fastin().rstrip()
cnt = 0         
func(n, cnt)