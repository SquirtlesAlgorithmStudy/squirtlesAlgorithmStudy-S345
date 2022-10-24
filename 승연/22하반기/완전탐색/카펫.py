# 갈색이 노란색보다 행, 열이 각 2씩 더 많음
# 가로 * 세로 = 노란색 + 갈색

# 실수한 부분 : yellow 카펫의 갯수 검증해줘야 함 (x-2)(y-2)==yellow (테두리 빼고 yellow)
def solution(brown, yellow):
    total = brown + yellow
    
    minimum_dict = {}
    for i in range(1, total):
        if total % i == 0:
            row = total // i
            if (row - 2) * (i - 2) == yellow:
                minimum_dict[abs(row - i)] = [row, i]

    min_key = min(list(minimum_dict.keys()))
    answer = sorted(minimum_dict[min_key], reverse = True)
    
    return answer