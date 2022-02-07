N = int(input())
remain = 0

if (N % 3) == 0 or (N % 5) == 0 or (N % 8) == 0 or ((N % 3) % 5) == 0:
    if N >= 5:
        numSuger = N // 5
        remain = (N % 5)
        if remain == 1:
            print((numSuger-1) + 2)
        elif remain == 2:
            print((numSuger-2) + 4)
        elif remain == 3:
            print(numSuger+1)
        elif remain == 4:
            print((numSuger-1)+3)
        else:
            print(numSuger)
    else:
        print(1)
else:
    print(-1)