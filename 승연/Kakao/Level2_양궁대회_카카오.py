from itertools import combinations_with_replacement


def solution(n, info):
    answer = [0 for _ in range(11)]
    win = False

    # 라이언이 이길 때 최대 점수 차이
    max_num = 0
    # 중복 조합 이용해 라이언의 점수 만들기. res에는 맞춘 과녁의 정보가 들어감
    for res in list(combinations_with_replacement(range(0, 11), n)):
        Ryan_info = [0 for _ in range(11)]
        for r in res:
            Ryan_info[10 - r] += 1
        Ryan = 0
        peach = 0
        # 라이언 점수와 어피치 점수 비교
        # i는 인덱스 정보, l,p에는 해당 인덱스에 대응되는 값
        for i, (l, p) in enumerate(zip(Ryan_info, info)):
            if l == p == 0:
                continue
            if p >= l:
                peach += (10 - i)
            elif l > p:
                Ryan += (10 - i)
        # 총 점수를 비교해 라이언이 큰 경우 결과를 업데이트
        if Ryan > peach:
            win = True
            if (Ryan - peach) > max_num:
                max_num = Ryan - peach
                answer = Ryan_info
    if not win:
        return [-1]
    return answer
