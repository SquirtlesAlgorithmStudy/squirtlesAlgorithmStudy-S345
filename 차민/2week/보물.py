n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
result = 0
cnt = 0

sub_a = sorted(a, reverse=True)
sub_b = sorted(b)

for i in range(n):
  a[i]=sub_a[sub_b.index(b[i])]
  sub_a.remove(sub_a[sub_b.index(b[i])])
  sub_b.remove(b[i])

c=[x*y for x,y in zip(a,b)]
for i in c:
  result+=i

print(result)