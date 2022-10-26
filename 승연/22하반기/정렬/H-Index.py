# 이것도 간단한 문제인데, 처음에 문제를 제대로 이해 못해서 시간이 좀 걸렸다.
# 급할수록 문제 확실히 이해하고 풀기
def solution(citations):
    citations.sort(reverse = True)
    count, answer = 0, 0
    for i in range(max(citations), -1, -1):
        # i를 max값부터 하나씩 줄여가며 그 값보다 큰 값이 i개 이상 있는지 센다.
        for j in citations:
            if i <= j:
                count += 1
        # i보다 크거나 같은 값이 i개 이상 크거나 같아지는 순간 break
        if count >= i:
            answer = i
            break
        else:
            count = 0
    return answer