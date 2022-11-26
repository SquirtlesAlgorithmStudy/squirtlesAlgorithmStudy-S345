import sys
input = sys.stdin.readline

question = input().rstrip()

accumulated_data = 0
accumulated_list = []

buffer = ""

for character in question:
    if character == "+":
        accumulated_data += int(buffer)
        buffer = ""
    
    elif character == "-":
        accumulated_data += int(buffer)
        buffer = ""
        accumulated_list.append(accumulated_data)
        accumulated_data = 0

    else:
        buffer += character

accumulated_data += int(buffer)
accumulated_list.append(accumulated_data)

result = accumulated_list[0]
for data in accumulated_list[1:]:
    result -= data

print(result)
