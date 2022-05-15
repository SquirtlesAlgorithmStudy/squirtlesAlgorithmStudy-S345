import sys
input = sys.stdin.readline

# make1 = 1
# make2 = 11, 2
# make3 = 111, 21
# make4 = 1111, 22, 211
# make5 = 11111, 221, 2111, 50
# make6 = 111111, 222, 2211, 21111, 51
# make7 = 1111111, 2221, 22111, 211111, 511, 52

#2, 3, 6 -> 12
#make 1 = 0
#make 2 = 1 : 2
#make 3 = 1 : 3
#make 4 = 0
#make 5 = 1 : 23
#make 6 = 2 : 222, 33

#make 7 = 1 : 223
#make 8 = 2222, 233, 26
#make 9 = 2223, 333, 36

#dp[0] = 0
#dp[1] = 0
#dp[2] = 1


n, won = map(int, input().split())
values =[0] * (n+1)
r = [0] * (n+1)
for i in range(1,n+1):
  wons[i] = int(input())

dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range (2, n+1):
    for j in range():
