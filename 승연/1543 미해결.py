Document = input()
Finding = input()
N = 0
i = 0

for k in range(len(Document)):
    if Document[k] == Finding[0]:
        fistSame = k
        break

Document = Document[fistSame:]

while(True):
    NumSame = 0
    HeadIndex = 0

    if len(Document) < len(Finding):
        break

    for j in range(len(Finding)):
        if Document[j] == Finding[j]:
            NumSame += 1
        if Document[j] == Finding[0]:
            HeadIndex = j

    if NumSame == len(Finding):
        N += 1
        if len(Document) == len(Finding):
            break
        else:
            Document = Document[len(Finding):]
    elif HeadIndex == 0:
        if len(Document) == len(Finding):
            break
        else:
            Document = Document[len(Finding):]
    else:
        if len(Document) == len(Finding):
            break
        else:
            Document = Document[HeadIndex:]

print(N)