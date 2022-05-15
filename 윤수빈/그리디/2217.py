n = int(input())
data = []
result = []

for i in range(n):
    x = int(input())
    data.append(x)

data.sort(reverse=True)

for i in range(n):
    result.append((i + 1) * data[i])
    
print(max(result))
