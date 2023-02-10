from collections import deque

def rolling_dice(a,b,cmd):
    global x, y

    if 0 <= a <= n-1 and 0 <= b <= m-1:

        if cmd == 4:
            dice.rotate(-1)
        elif cmd == 3:
            dice.rotate(1)
        elif cmd == 2:
            tmp = dice[1]
            dice[1] = dice_side[0]
            dice_side[0] = dice[3]
            dice[3] = dice_side[1]
            dice_side[1] = tmp
        else:
            tmp = dice[1]
            dice[1] = dice_side[1]
            dice_side[1] = dice[3]
            dice[3] = dice_side[0]
            dice_side[0] = tmp

        if graph[a][b]:
            dice[1] = graph[a][b]
            graph[a][b] = 0
        else:
            graph[a][b] = dice[1]
        x = a
        y = b
        print(dice[3])
    else:
        return
n, m, x, y, k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cmds = list(map(int,input().split()))
dx, dy = [0,0,0,-1,1], [0,1,-1,0,0]
dice = deque([0 for _ in range(4)])
dice_side = deque([0 for _ in range(2)])

for cmd in cmds:
    rolling_dice(x+dx[cmd],y+dy[cmd],cmd)
    
#54782775	grvty0717	 14499	맞았습니다!!	34148	68	Python 3 / 수정	1097	19초 전
