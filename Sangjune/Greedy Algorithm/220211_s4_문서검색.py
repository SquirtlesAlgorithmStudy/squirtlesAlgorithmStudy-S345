import sys

s = str(sys.stdin.readline().strip())
voc = str(sys.stdin.readline().strip())
count = 0

isIn = voc in s

while isIn == True:
    s = s.replace(voc, "", 1).strip()
    count += 1
    isIn = voc in s

print(count)