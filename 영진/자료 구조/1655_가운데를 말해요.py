import sys,heapq
N=int(sys.stdin.readline())

left_heap=[]
right_heap=[]
for _ in range(N):
    num=int(sys.stdin.readline())
    if len(left_heap)==len(right_heap):
        heapq.heappush(left_heap,-num)
    else:
        heapq.heappush(right_heap,num)
        
    if right_heap and right_heap[0]<-left_heap[0]:
        left_tmp=heapq.heappop(left_heap)
        right_tmp=heapq.heappop(right_heap)
        
        heapq.heappush(left_heap,-right_tmp)
        heapq.heappush(right_heap,-left_tmp)
        
    print(-left_heap[0])