document = list(input()) #5
word = list(input()) #2

cnt = 0
back = 0

ascii_docu = []
ascii_word = []

for character in document:
  ascii_docu.append(ord(character))

for character in word:
  ascii_word.append(ord(character))
  

for i in range(len(ascii_docu)):
  for j in range(len(ascii_word)):
    if ascii_docu[i] != ascii_word[j]:
      print(i, ": ", ascii_docu[i]," ", ascii_word[j])
      break
  cnt += 1

    

print(document)
print(cnt)