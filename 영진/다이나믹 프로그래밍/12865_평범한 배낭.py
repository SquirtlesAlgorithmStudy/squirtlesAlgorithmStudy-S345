N, K = map(int, input().split())
stuff = [[0, 0]]
for _ in range(N):
    stuff.append(list(map(int, input().split())))

knpsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            knpsack[i][j] = knpsack[i-1][j]
        else:
            knpsack[i][j] = max(knpsack[i-1][j-weight]+value, knpsack[i-1][j])


print(knpsack[N][K])
