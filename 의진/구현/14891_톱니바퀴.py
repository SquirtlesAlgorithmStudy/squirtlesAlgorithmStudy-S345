import sys
fastin = sys.stdin.readline

sawtoothes = [fastin().rstrip() for _ in range(4)]
k = int(fastin())
rotates = [tuple(map(int, fastin().rstrip().split())) for _ in range(k)]


def update_status(sawtoothes):
    status = [bool(int(sawtoothes[i][2])) ^ bool(int(sawtoothes[i+1][6]))
              for i in range(3)]
    return status


def circularShift_left(a):
    result_list = ['0'] * 8
    for i in range(8):
        result_list[i-1] = a[i]
    result = ''.join(result_list)
    return result


def circularShift_right(a):
    result_list = ['0'] * 8
    for i in range(7):
        result_list[i+1] = a[i]
    result_list[0] = a[7]
    result = ''.join(result_list)
    return result


def circularShift(a, direction):
    if direction == 1:
        return circularShift_right(a)
    else:
        return circularShift_left(a)


for rotate in rotates:
    status = update_status(sawtoothes)

    if rotate[0] == 1:
        sawtoothes[0] = circularShift(sawtoothes[0], rotate[1])
        i = 0
        while(True):
            if i == 3:
                break
            if status[i]:
                sawtoothes[i+1] = circularShift(sawtoothes[i+1],
                                                ((-1) ** (i+1)) * rotate[1])
            else:
                break
            i += 1
    elif rotate[0] == 4:
        sawtoothes[3] = circularShift(sawtoothes[3], rotate[1])
        i = 2
        while(True):
            if i == -1:
                break
            if status[i]:
                sawtoothes[i] = circularShift(sawtoothes[i],
                                              ((-1) ** (i+1)) * rotate[1])
            else:
                break
            i -= 1
    elif rotate[0] == 2:
        sawtoothes[1] = circularShift(sawtoothes[1], rotate[1])
        i = 1
        while(True):
            if i == 3:
                break
            if status[i]:
                sawtoothes[i+1] = circularShift(sawtoothes[i+1],
                                                ((-1) ** (i)) * rotate[1])
            else:
                break
            i += 1
        i = 0
        while(True):
            if i == -1:
                break
            if status[i]:
                sawtoothes[i] = circularShift(sawtoothes[i],
                                              ((-1) ** (i+1)) * rotate[1])
            else:
                break
            i -= 1
    elif rotate[0] == 3:
        sawtoothes[2] = circularShift(sawtoothes[2], rotate[1])
        i = 2
        while(True):
            if i == 3:
                break
            if status[i]:
                sawtoothes[i+1] = circularShift(sawtoothes[i+1],
                                                ((-1) ** (i+1)) * rotate[1])
            else:
                break
            i += 1
        i = 1
        while(True):
            if i == -1:
                break
            if status[i]:
                sawtoothes[i] = circularShift(sawtoothes[i],
                                              ((-1) ** (i)) * rotate[1])
            else:
                break
            i -= 1

print(int(sawtoothes[0][0]) + 2 * int(sawtoothes[1][0]) +
      4 * int(sawtoothes[2][0]) + 8 * int(sawtoothes[3][0]))
