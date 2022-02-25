k = int(input())
rope_weight = []
rope_weight_max = []

for i in range(k):
  rope_weight.append(int(input()))

rope_weight.sort(reverse=True)

for x in range(k):
  rope_weight_max.append(rope_weight[x]*(x+1))

rope_weight_max.sort(reverse=True)

print(rope_weight_max[0])
  



  