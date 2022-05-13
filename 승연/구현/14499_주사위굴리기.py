#BaekJoon 14499 주사위 굴리기
import sys
input = sys.stdin.readline

N, M, x, y, movement = map(int, input().split())

# 주의 ! 아래의 방법으로 배열을 선언하게 되면, 단순히 요소를 복사하게 되는 얕은 복사가 일어남.
# shallow copy가 발생하면 바라보는 객체는 동일하기 때문에 값을 변경하면 다른 원소들도 값이 변경되는 현상 발생
# mapGraph = [[0]*M]*N

# 이 방법 사용하기 (N행 M열)
mapGraph = [[0 for col in range(M)] for row in range(N)]
movements = []

for i in range(N):
    temp = list(input().split())
    for j in range(M):
        mapGraph[i][j] = int(temp[j])


movements = list(input().split())

dice = {'동': 0, '서': 0, '남': 0, '북': 0, '밑': 0, '위': 0}
dice_temp = {'동': 0, '서': 0, '남': 0, '북': 0, '밑': 0, '위': 0}

for move in movements:
    if move == '1': #동쪽으로 이동
        y += 1
        # 주사위가 바깥으로 나가는 경우 예외처리 -> x, y값으로 판단 "mapGraph"인덱스 안에 있는지?
        if y >= M:
            y -= 1
            continue
        #주사위 동서남북밑위 변하는 부분 처리
        dice_temp['동'] = dice['위']
        dice_temp['서'] = dice['밑']
        dice_temp['밑'] = dice['동']
        dice_temp['위'] = dice['서']
        # 무조건 지도상의 숫자가 주사위 밑면에 복사되고 0으로 변하는데, 0인 경우는 주사위의 밑면 숫자가 복사됨
        if mapGraph[x][y] == 0:
            mapGraph[x][y] = dice_temp['밑']
        else:
            dice_temp['밑'] = mapGraph[x][y]
            mapGraph[x][y] = 0
        print(dice_temp['위'])
        dice['동'] = dice_temp['동']
        dice['서'] = dice_temp['서']
        dice['밑'] = dice_temp['밑']
        dice['위'] = dice_temp['위']

    if move == '2':  # 서쪽으로 이동
        y -= 1
        # 주사위가 바깥으로 나가는 경우 예외처리 -> x, y값으로 판단 "mapGraph"인덱스 안에 있는지?
        if y < 0:
            y += 1
            continue
        # 주사위 동서남북밑위 변하는 부분 처리
        dice_temp['동'] = dice['밑']
        dice_temp['서'] = dice['위']
        dice_temp['밑'] = dice['서']
        dice_temp['위'] = dice['동']
        # 무조건 지도상의 숫자가 주사위 밑면에 복사되고 0으로 변하는데, 0인 경우는 주사위의 밑면 숫자가 복사됨
        if mapGraph[x][y] == 0:
            mapGraph[x][y] = dice_temp['밑']
        else:
            dice_temp['밑'] = mapGraph[x][y]
            mapGraph[x][y] = 0
        print(dice_temp['위'])
        dice['동'] = dice_temp['동']
        dice['서'] = dice_temp['서']
        dice['밑'] = dice_temp['밑']
        dice['위'] = dice_temp['위']

    if move == '3': #북쪽으로 이동
        x -= 1
        # 주사위가 바깥으로 나가는 경우 예외처리 -> x, y값으로 판단 "mapGraph"인덱스 안에 있는지?
        if x < 0:
            x += 1
            continue
        #주사위 동서남북밑위 변하는 부분 처리
        dice_temp['남'] = dice['밑']
        dice_temp['북'] = dice['위']
        dice_temp['밑'] = dice['북']
        dice_temp['위'] = dice['남']
        # 무조건 지도상의 숫자가 주사위 밑면에 복사되고 0으로 변하는데, 0인 경우는 주사위의 밑면 숫자가 복사됨
        if mapGraph[x][y] == 0:
            mapGraph[x][y] = dice_temp['밑']
        else:
            dice_temp['밑'] = mapGraph[x][y]
            mapGraph[x][y] = 0
        print(dice_temp['위'])
        dice['남'] = dice_temp['남']
        dice['북'] = dice_temp['북']
        dice['밑'] = dice_temp['밑']
        dice['위'] = dice_temp['위']

    if move == '4': #남쪽으로 이동
        x += 1
        # 주사위가 바깥으로 나가는 경우 예외처리 -> x, y값으로 판단 "mapGraph"인덱스 안에 있는지?
        if x >= N:
            x -= 1
            continue
        #주사위 동서남북밑위 변하는 부분 처리
        dice_temp['남'] = dice['위']
        dice_temp['북'] = dice['밑']
        dice_temp['밑'] = dice['남']
        dice_temp['위'] = dice['북']
        # 무조건 지도상의 숫자가 주사위 밑면에 복사되고 0으로 변하는데, 0인 경우는 주사위의 밑면 숫자가 복사됨
        if mapGraph[x][y] == 0:
            mapGraph[x][y] = dice_temp['밑']
        else:
            dice_temp['밑'] = mapGraph[x][y]
            mapGraph[x][y] = 0
        print(dice_temp['위'])
        dice['남'] = dice_temp['남']
        dice['북'] = dice_temp['북']
        dice['밑'] = dice_temp['밑']
        dice['위'] = dice_temp['위']