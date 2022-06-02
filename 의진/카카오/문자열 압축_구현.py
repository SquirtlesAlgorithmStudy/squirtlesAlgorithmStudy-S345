def solution(s):
    answer = 0
    result = []

    for i in range(len(s)):
        i += 1
        number = len(s)
        j = 0
        while True:
            cnt = 0
            for k in range(1, (len(s)//i) - j):
                if s[i*j:(i*j)+i] == s[i*(j+k):(i*(j+k)+i)]:
                    cnt += 1
                    number -= i

                else:
                    break
            if cnt > 0:
                number += (len(str(cnt+1)))
            j += (cnt + 1)
            if j >= (len(s) - i):
                break
        result.append(number)
    answer = min(result)
    return answer
