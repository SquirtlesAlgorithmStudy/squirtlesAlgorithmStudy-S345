def solution(survey, choices):
    score_dict = do_test(survey, choices)
    answer = find_answer(score_dict)
    return answer


def do_test(survey, choices):
    score_dict = {'R': 0, 'T': 0, 'C': 0,
                  'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for test in zip(survey, choices):
        if test[1] < 4:
            score_dict[test[0][0]] += (4 - test[1])
        elif test[1] > 4:
            score_dict[test[0][1]] += test[1] - 4

    return score_dict


def find_answer(score_dict):
    answer = ''
    for item in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        if score_dict[item[0]] < score_dict[item[1]]:
            answer += item[1]
        else:
            answer += item[0]

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
