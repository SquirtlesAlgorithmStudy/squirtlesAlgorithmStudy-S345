# 문법 찾아봄 
s = input()
find = input()
find_length = len(find)
count = 0
i = 0
while i < len(s):
    if s[i : i + find_length] == find:
        count += 1
        i += find_length
    else:
        i += 1
print(count)

