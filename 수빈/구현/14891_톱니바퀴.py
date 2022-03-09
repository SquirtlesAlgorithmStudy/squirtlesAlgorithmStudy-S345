import sys
fastin = sys.stdin.readline

def findRotatingGear(target, direction):
    global gears     #글로벌 변수
    res = [0]*4
    
    res[target] = direction
    
    # target을 기준으로 왼쪽 검사
    for i in range(target-1, -1, -1):
        if gears[i][2] ==gears[i+1][6]:
            break
        res[i] = res[i+1]*(-1)
        
    # target을 기준으로 오른쪽 검사
    for i in range(target+1, 4):
        if gears[i][6] ==gears[i-1][2]:
            break
        
        res[i] = res[i-1]*(-1)
        
    return res

def rotate(res):
    global gears    #글로벌 변수
    
    for i in range(4):
        if res[i]==0:
            continue
        elif res[i]==1:
            gears[i] = [gears[i][7]] + gears[i][0:7]
        else:
            gears[i] = gears[i][1:8] + [gears[i][0]]
            
if __name__=="__main__":
    gears = [list(map(int, list(fastin().strip()))) for _ in range(4)]
    # gears에 톱니바퀴의 N/S극 정보를 모두 넣고. 리스트로. 4번 input을 받아서.
    
    k = int(fastin().strip())
    # 그 다음줄에 몇 번 회전할 것인지 input으로 받기
    
    rotatingInfo = [tuple(map(int, fastin().strip().split())) for _ in range(k)]
    #회전 방법은 튜플로 받기. k개의 줄로 input이 들어옴.
    
    for g,d in rotatingInfo:
        res = findRotatingGear(g-1, d)
        rotate(res)
        
    score = gears[0][0] + gears[1][0]*2 + gears[2][0]*4 + gears[3][0]*8
    
    print(score)
    
#전체적으로 이 res 가 잘 이해가 안가는데...
    



1. 처음 톱니바퀴가 움직이기 전에, 인접한 톱니바퀴가 움직일 수 있는지 없는지를 "전부" 검사한 뒤에 톱니바퀴를 움직일 수 있다.
2.인접한 톱니바퀴의 인접한 톱니바퀴도 "전부" 검사해야 한다.
3. '회전 여부'를 결정짓는 '인접한 톱니바퀴의 톱날'은 index2번과 6번이다.([0], [6])
4. 주어진 톱니바퀴는 일단 회전하는 것이 전제되어 있다. 
인접 톱니바퀴가 전부 회전하지 않는다 해도, 처음 주어진 톱니바퀴는 반드시 회전해야만 한다.
5. 인접한 톱니바퀴는 주어진 톱니바퀴와 반대 방향으로 회전해야 한다.

ㅎ회전 자체는 deque의 rotate 함수를 사용하면 된다. 
ㅅ시계방향은 1, 반시계 방향은 -1을 파라미터로 넣으면 된다.