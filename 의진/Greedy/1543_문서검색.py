import sys
fastin = sys.stdin.readline

document = fastin()
query = fastin()
result = 0

len_query = len(query)-1

i = 0
while(i < len(document) - len_query):
  if document[i] == query[0]:
    j = i
    while(True):
      if j + 1 - i == len_query : 
        result += 1
        i += len_query
        break
      else:
        j += 1
        if document[j] != query[j-i]:
          i += 1
          break
  else : i += 1
  
print(result)