import sys
fastin = sys.stdin.readline

def findRotatingGear(target, direction):
    global gears
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
    global gears
    
    for i in range(4):
        if res[i]==0:
            continue
        elif res[i]==1:
            gears[i] = [gears[i][7]] + gears[i][0:7]
        else:
            gears[i] = gears[i][1:8] + [gears[i][0]]
            
if __name__=="__main__":
    gears = [list(map(int, list(fastin().strip()))) for _ in range(4)]
    
    k = int(fastin().strip())
    
    rotatingInfo = [tuple(map(int, fastin().strip().split())) for _ in range(k)]
    
    for g,d in rotatingInfo:
        res = findRotatingGear(g-1, d)
        rotate(res)
        
    score = gears[0][0] + gears[1][0]*2 + gears[2][0]*4 + gears[3][0]*8
    
    print(score)