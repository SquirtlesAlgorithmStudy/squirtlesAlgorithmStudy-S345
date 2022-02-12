# 1543

docu = input()
find = input()
count = 0
index = 0
while(True):
    if index > len(docu):
        break
    
    if docu[index:index+len(find)] == find:
        count = count + 1
        index = index + len(find)
        
    else:
        index = index + 1

print(count)