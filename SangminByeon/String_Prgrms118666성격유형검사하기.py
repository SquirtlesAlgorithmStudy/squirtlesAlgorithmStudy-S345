def solution(survey, choices):
    answer = []
    score_R, score_T = 0,0
    score_C, score_F = 0,0
    score_J, score_M = 0,0
    score_A, score_N = 0,0

    for i in range(len(survey)):
        latter = survey[i][1]
        choice = choices[i]-4 #어차피 각 쌍끼리의 높낮음만 비교하면 됨.

        if latter == "R":
            score_R += choice
        elif latter == "T":
            score_T += choice
        elif latter == "C":
            score_C += choice
        elif latter == "F":
            score_F += choice
        elif latter == "J":
            score_J += choice
        elif latter == "M":
            score_M += choice
        elif latter == "A":
            score_A += choice
        elif latter == "N":
            score_N += choice

    ## 파이썬에서는 `condition ? value_if_true : value_if_false` 문법이 쓰이지 않는다.
    # score_R >= score_T ? answer.append('R') : answer.append('T')
    # score_C >= score_F ? answer.append('C') : answer.append('F')
    # score_J >= score_M ? answer.append('J') : answer.append('M')
    # score_A >= score_N ? answer.append('A') : answer.append('N')

    answer.append('R' if score_R >= score_T else 'T')
    answer.append('C' if score_C >= score_F else 'F')
    answer.append('J' if score_J >= score_M else 'M')
    answer.append('A' if score_A >= score_N else 'N')

    # print(score_R, score_T, '\n', score_C, score_F, '\n', score_J, score_M, '\n', score_A, score_N)


    return ''.join(answer)