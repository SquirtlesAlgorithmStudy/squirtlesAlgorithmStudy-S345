import sys
fastin = sys.stdin.readline

N, M = map(int, fastin().rstrip().split())
g = [list(fastin().rstrip()) for _ in range(N)]
