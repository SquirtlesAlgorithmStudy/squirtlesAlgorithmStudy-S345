import heapq
import time

a = [i for i in range(1000000)]
heap = [i for i in range(10000000, 0, -1)]
heapq.heapify(heap)
start = time.time()
for item in a:
    heapq.heapreplace(heap, item)
elapsed_time_1 = time.time() - start

a = [i for i in range(1000000)]
heap = [i for i in range(10000000, 0, -1)]
heapq.heapify(heap)
start = time.time()
for item in a:
    heapq.heappop(heap)
    heapq.heappush(heap, item)
elapsed_time_2 = time.time() - start

print(elapsed_time_1)
print(elapsed_time_2)
