# https://www.acmicpc.net/problem/2941
cS = ["c=","c-","dz=","d-","lj", "nj","s=","z="]

S = input()
count = 0
i = 0
while i < len(S):
    # print(i)
    if S[i:i+2] in cS:
        # print("i~i+2",S[i:i+2])
        count += 1
        i += 2
    elif S[i:i+3] in cS:
        # print("i~i+3",S[i:i+3])
        count += 1
        i += 3
    else:
        count += 1
        # print("i",S[i])
        i += 1
print(count)