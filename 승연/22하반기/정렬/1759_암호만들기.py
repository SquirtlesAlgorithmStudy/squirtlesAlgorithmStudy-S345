# 암호만들기

# 최소 한 개의 모음 (a e i o u)
# 최소 두 개의 자음
# 오름차순

import sys
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())

alphabets = input().split()
mo = ['a', 'e', 'i', 'o', 'u']

mos = []
zhas = []
for i in alphabets:
    if i in mo:
        mos.append(i)
    else:
        zhas.append(i)

combi = []
for com in combinations(alphabets, L):
    tmp = com.count('a')+com.count('e')+com.count('i')+com.count('o')+com.count('u')
    if tmp < 1 or tmp > (L-2):
        continue
    else:
        combi.append(''.join(com))

# 각각의 값 알파벳순 1차 정렬
for i in range(len(combi)):
    combi[i] = ''.join(sorted(combi[i]))

# 전체 알파벳순 2차 정렬
combi.sort()

for i in combi:
    print(''.join(i))