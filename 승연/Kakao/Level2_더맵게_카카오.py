import heapq

def solution(scoville, K):
    # 리스트를 힙 구조로 변환
    heapq.heapify(scoville)
    result = 0

    while len(scoville) >= 2 :
        # 힙에서 최솟값
        min_ = heapq.heappop(scoville) 
        # 액체의 최솟값이 K보다 크다는 조건 만족
        if min_ >= K: 
            return result 
        # 두 번째로 작은 값 가져와서 두 배를 한 후 가장 작은 값과 합친 값을 힙에 삽입
        else: 
            min_2 = heapq.heappop(scoville) 
            heapq.heappush(scoville, min_ + (min_2 * 2))
            result += 1
  
    if scoville[0] > K:
        return result

    else:
        return -1