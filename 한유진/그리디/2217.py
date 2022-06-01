# 반례확인 하면서 답 도출과정도 확인 ㅜ ㅜ..
n = int(input())
rope = list()
for _ in range(n):
    rope.append(input())
rope.sort()
answer = 0
for i in rope:
    answer = max(answer, i * n)
    n -= 1