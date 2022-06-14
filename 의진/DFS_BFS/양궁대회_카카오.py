import copy
answer = [-1]
maxdScore = 0


def isPriority(ryan):
    for i in range(10, -1, -1):
        if ryan[i] > answer[i]:
            return True
        elif ryan[i] < answer[i]:
            return False


def updateMaxScore(apeach, ryan):
    global maxdScore
    global answer
    ryanScore = 0
    apeachScore = 0
    for i in range(11):
        if ryan[i] > apeach[i]:
            ryanScore += 10 - i
        elif apeach[i] > 0:
            apeachScore += 10 - i

    dScore = ryanScore - apeachScore
    if dScore > 0 and dScore >= maxdScore:
        if maxdScore == dScore and not isPriority(ryan):
            return
        maxdScore = dScore
        answer = copy.deepcopy(ryan)  # (기존에 있던 값을 바꾸는 것 - global)
        # global 안 걸어주면 -> 지역변수가 새로 선언되는 것! -> 거기에
        # DEEPCOPY된 Ryan이 새로운 지역변수에 저장된다.


def dfs(score, arrowNum, apeach, ryan):
    if score == 11 or arrowNum == 0:
        ryan[10] += arrowNum
        updateMaxScore(apeach, ryan)
        ryan[10] -= arrowNum
        return

    if apeach[score] < arrowNum:
        ryan[score] += apeach[score] + 1
        dfs(score + 1, arrowNum - apeach[score]-1, apeach, ryan)
        ryan[score] -= apeach[score] + 1

    dfs(score + 1, arrowNum, apeach, ryan)


def solution(n, info):
    ryan = [0] * 11
    dfs(0, n, info, ryan)
    return answer


n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

print(solution(n, info))
