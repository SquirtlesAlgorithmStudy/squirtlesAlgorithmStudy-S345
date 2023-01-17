import sys 

N = sys.stdin.readline

array = [[0]*101 for _ in range(101) ]

#check 1 otherwise 0 and sum all 1's 

for i in range(int(N)):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            array[x+i][y+j] =1 
        
    
sum = 0
for i in array:
    result += sum(i)
result = sum
    
print(result)