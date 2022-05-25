
import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

N, M, K = map(int, input().rstrip().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip().split())))

# 초기 주사위 좌표
dice = [2,4,1,3,5,6]
d = 0

def change_dice(dice, d):
    #동쪽 이동
    if d==0:
        #dice = [2,6,4,1,5,3]
        dice[1]=dice[2]
