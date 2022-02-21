n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
result = 0

sub_a = sorted(a, reverse=True)
sub_b = sorted(b)


c=[x*y for x,y in zip(sub_a,sub_b)]
for i in c:
  result+=i

print(result)