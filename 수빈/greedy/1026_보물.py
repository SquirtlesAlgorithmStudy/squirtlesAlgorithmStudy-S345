import sys
fastin = sys.stdin.readline
  
# n = int(fastin())
# a = list(map(int, fastin().rstrip().split()))
# b = list(map(int, fastin().rstrip().split()))
n=5
a=[1,1,1,6,0]
b=[2,7,8,3,1]
result =0

a.sort()
print(b)

# print(b,b.pop(b.index(max(b))))

for i in range(len(a)):
  # print(a[i], b.pop(b.index(max(b))))
  result += a[i]*(b.pop(b.index(max(b))))
print(result)


# sort()는 리스트자체를 정렬해버리기때문에 정렬된 객체를 생성하는 sorted()를 써야해요