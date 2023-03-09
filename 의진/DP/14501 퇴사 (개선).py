n = int(input())

t_list = []
p_list = []
answer = [0] * (n + 1)

for i in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

for i in range(n - 1, -1, -1):
    if t_list[i] + i > n:
        answer[i] = answer[i + 1]
    else:
        answer[i] = max(p_list[i] + answer[i + t_list[i]], answer[i + 1])

print(answer[0])
