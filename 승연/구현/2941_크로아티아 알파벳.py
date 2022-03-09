import sys

fastin = sys.stdin.readline
word = str(fastin().rstrip())

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    word = word.replace(i, '.')  
print(len(word))