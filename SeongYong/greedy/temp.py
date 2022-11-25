prob = input().split('-')

sum = 0

for i in prob[1:]:
    for j in i.split('+'):
        sum -=int(j)
        
sum += int(prob[0].split('-'))
print(sum)


