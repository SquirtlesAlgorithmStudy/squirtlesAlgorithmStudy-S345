## 시도 1
import sys 
fastin = sys.stdin.readline

a, b = map(int, fastin().rstrip().split())
cnt = 0

while True:
    
    if abs(a-b)>a:
        a *=2
        print('첫 번째 if문',a)
        
    elif b>a:
        if(abs(2*a-b)<abs(a-b)):
            a *=2
            print('두 번째 if문', a)
        else:
            a+=1
            print('세 번째 if문', a)
    elif b<a:
        a -=1
        print('네 번째 if문', a)
    elif a==b:
        break
    
    cnt +=1
    print('while문 안에 cnt', cnt)

print('최종', cnt)

## 시도2
import sys 
fastin = sys.stdin.readline
from collections import deque

a, b = map(int, fastin().rstrip().split())
MAX = 10 **5
option = [0]*(MAX+1)


def BFS():
    q = deque()   # q변수를 deque()로 초기화
    q.append(a)
    print('q는 ', q)
    while q:
        x = q.popleft()
        if x==b:
            print('option은 ',option[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=MAX and not option[nx]:
                option[nx] = option[x] +1
                print('option[x]은 ',option[x])
                q.append(nx)
                print('option[nx]는 ',option[nx])
                
    
BFS()
