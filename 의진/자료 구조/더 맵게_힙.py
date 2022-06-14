import heapq
from collections import deque


def mixing(scoville):
    temp1 = heapq.heappop(scoville)
    temp2 = heapq.heappop(scoville)
    temp = temp1 + 2 * temp2
    heapq.heappush(scoville, temp)
    return scoville


def solution(scoville, K):

    answer = 0
    scoville.sort()
    while True:
        if len(scoville) <= 1:
            if (scoville[0] >= K):
                return answer
            else:
                return -1
        min_value = heapq.heappop(scoville)
        if min_value >= K:
            return answer
        heapq.heappush(scoville, min_value)
        scoville = mixing(scoville)
        answer += 1
