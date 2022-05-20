n, k = map(int,input().split())
result = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            result += str(k) in f"{h:02d}{m:02d}{s:02d}"
            
print(result)
