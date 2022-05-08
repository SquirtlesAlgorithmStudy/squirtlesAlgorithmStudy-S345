# 1543- 문서 검색

docs = input()
word = input()

count = 0
index = 0

while index <= len(docs) - len(word) :      # 검색하려는 길이보다 적게 남으면 멈춤
        if docs[index: index + len(word)] == word :
            count += 1
            index += len(word)              # 검색하고자 하는 워드 수 만큼 index 증가
        else :
            index += 1                      # 찾지 못한 경우 index 1 증가
print(count)
            