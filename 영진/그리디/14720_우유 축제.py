from sys import stdin
N=int(input())
shop=list(map(int,stdin.readline().rstrip().split()))

state=0
milk=0
for i in range(len(shop)):
    if state==shop[i]:
        state+=1
        milk+=1
        state=state%3

print(milk)