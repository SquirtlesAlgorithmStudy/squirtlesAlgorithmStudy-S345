# N시 59분 59초까지 K포함된 시각의 수
N, K = input().split() #int로 받으면 너무 복잡해짐
N = int(N) + 1
count = 0

for i in range(N):
    if i < 10:
        ii = '0' + str(i)
    else:
        ii = str(i)
    for k in range(60):
        if k < 10:
            kk = '0' + str(k)
        else:
            kk = str(k)
        for j in range(60):
            if j < 10:
                jj = '0' + str(j)
            else:
                jj = str(j)
            if K in (ii + kk + jj):
                count += 1
print(count)
