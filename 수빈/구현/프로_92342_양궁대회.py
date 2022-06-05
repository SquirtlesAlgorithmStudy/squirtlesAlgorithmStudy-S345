from itertools import combinations_with_replacement
# itertools 라이브러리를 이용하면 조합과 순열을 쉽게 구할 수 있음
## 관련 개념설명 링크 : https://seu11ee.tistory.com/5,  https://hyun-am-coding.tistory.com/entry/python-itertools%EC%97%90%EC%84%9C-Combinatoric-iterators%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0


def solution(n, info):
    answer = [0 for _ in range(11)]
    win = False
    max_num = 0 # 라이언이 이길 때 가장 큰 점수 차이
    # 1. 중복 조합을 이용해 라이언의 점수 만들기
    for res in list(combinations_with_replacement(range(0,11),n)):
        now = [0 for _ in range(11)]
        for r in res:
            now[10-r] +=1
        lion = 0
        peach = 0
        # 2. 라이언의 점수와 어피치의 점수를 비교
        for i, (l,p) in enumerate(zip(now, info)):
            if l == p == 0:
                continue
            if p >= l:
                peach += (10-i)
            elif l > p:
                lion += (10-i)
        # 3. 총 점수를 비교해 라이언이 더 큰 경우 결과를 업데이트
        if lion > peach:
            win = True
            if (lion-peach) > max_num:
                max_num = lion -peach
                answer = now
    if not win:
        return [-1]
    return answer