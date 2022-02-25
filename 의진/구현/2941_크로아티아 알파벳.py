import sys
fastin = sys.stdin.readline

inputString = fastin().rstrip()

i = 0
count = 0
while(i < len(inputString)):
    if inputString[i] == 'c':
        i += 1
        if i == len(inputString):
            count += 1
            break
        if inputString[i] == '=' or inputString[i] == '-':
            count += 1
            i += 1
        else:
            count += 1

    elif inputString[i] == 'd':
        i += 1
        if i == len(inputString):
            count += 1
            break
        if inputString[i] == '-':
            count += 1
            i += 1
        elif inputString[i] == 'z':
            i += 1
            if i == len(inputString):
                count += 2
                break
            if inputString[i] == '=':
                count += 1
                i += 1
            else:
                count += 2
        else:
            count += 1
    elif inputString[i] == 'l':
        i += 1
        if i == len(inputString):
            count += 1
            break
        if inputString[i] == 'j':
            count += 1
            i += 1
        else:
            count += 1
    elif inputString[i] == 'n':
        i += 1
        if i == len(inputString):
            count += 1
            break
        if inputString[i] == 'j':
            count += 1
            i += 1
        else:
            count += 1
    elif inputString[i] == 's':
        i += 1
        if i == len(inputString):
            count += 1
            break
        if inputString[i] == '=':
            count += 1
            i += 1
        else:
            count += 1
    elif inputString[i] == 'z':
        i += 1
        if i == len(inputString):
            count += 1
            break
        if inputString[i] == '=':
            count += 1
            i += 1
        else:
            count += 1
    else:
        i += 1
        count += 1

print(count)
