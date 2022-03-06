document = str(input())
word =  str(input())
d = len(document)
w = len(word)
count = 0
i = 0

while i in range(d):
    if i + w > d:
        break
    elif word[0:w] == document[i:i+w]:
        count += 1
        i += w
    else:
        i += 1
    
print(count)