# import sys
# fastin = sys.stdin.readline

# # n, k = map(int,input().split())
# m = []
# for i in range(n):
#     m.append(int(input()))

n = 10
k = 4790
m = [1,
     5,
     10,
     50,
     100,
     500,
     1000,
     5000,
     10000,
     50000]

i=0
c = 0 #사용한 동전의 개수를 count

for i in range(len(m)-1,0, -1):
  c += k//m[i]
  k = k%m[i]
  print(c, m[i],k)
  if k==0:
    break

print("답은",c)

# Q.백준 제출에는 왜 틀렸다고 뜨는지 모르겠음. input list를 잘못 받아온건가..?
