import sys 

n, m = map(int,input().split())
# 4 2 

stack =[]
def backtrack():
    if len(stack) == m : 
        print(" ".join(map(str,stack)))
        return 
    
    for i in range(1,n+1): 
        stack.append(i)
        backtrack()
        stack.pop()
    
backtrack()
    
    
#54633957	grvty0717	 15651	맞았습니다!!	30616	1400	Python 3 / 수정	286	