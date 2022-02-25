import sys

fin = sys.stdin.readline

s = fin().rstrip()

crAlp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for char in crAlp:
    s = s.replace(char, '_') # 한개로 취급
print(len(s))

# 함수 정리 
# string.count()
# string.find( , )