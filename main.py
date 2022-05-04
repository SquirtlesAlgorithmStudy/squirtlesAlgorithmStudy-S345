# #계단 수 
# n = int(input())
# #점수  
# arr = []
# for i in range(n):
#   arr.append(list(map(int,input().split())))

# print(arr)
# dp = []

# # d[1] = score[1]
# # d[2] = score[1]+score[2]

# # for i in range(3,n+1):
# #   d[i] = max(d[i-3]+score[i]+score[i-1], d[i-2]+score[i])

# # print(d[i])

# # #집의 수 
# # n= int(input())

# # #거리 
# # array = list(map(int,input().split()))



#포도잔 수 
n = int(input())
#포도주 양 
drink =[0]
for i in range(n):
  drink.append(int(input()))

d = [0]*100

d[1] = drink[1]

if n==1:
  print(d[n])

else:
  d[2] = drink[1] + drink[2]
  if n == 2:
    print(d[n])

  else:
    for i in range(4,n+1):
      d[i] = max(d[i-1], d[i-3]+drink[i-1]+drink[i], d[i-2]+drink[i])

    print(d[n])