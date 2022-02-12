import sys

s = str(sys.stdin.readline().strip())
voc = str(sys.stdin.readline().strip())
count = 0
idx = []
index = 0

while True:
    index = s.find(voc, index)
    if index == -1: break
    idx.append(index)
    index += len(voc)

print(len(idx))