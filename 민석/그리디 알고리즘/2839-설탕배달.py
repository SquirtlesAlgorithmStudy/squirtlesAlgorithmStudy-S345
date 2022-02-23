need = int(input())
a = 0
b = 0
k = [5, 3]

for sugar in k:

    if need % 3 == 0:
        a = need // 3
    elif need % sugar == 0:
        b = b + need // sugar
        need = need % sugar
        if a != 0 and a > b:
            print(b)
        else:
            print(a)
    else:
        print(-1)


# print(a)
#[a for sugar in k if need % sugar == 0 ]

#[a if need % sugar == 0 else '-1' for sugar in k]
