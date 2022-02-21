import sys
fastin = sys.stdin.readline
N, K = map(int, fastin().rstrip().split())

count = 0
if (N in range (24))& (K in range(1, 10)):
    for i in range(N +1):
        for j in range(60):
            for k in range(60):
                if str(K) in str(i) + str(j) + str(k):
                    count +=1                
elif (N in range (24))& (K == 0):
    for i in range(N +1):
        for j in range(60):
            for k in range(60):
                if len (str(i) + str(j) + str(k)) < 6:
                    count +=1
                elif str(K) in str(i) + str(j) + str(k):
                    count +=1
print(count)
