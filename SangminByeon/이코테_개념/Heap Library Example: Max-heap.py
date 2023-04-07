import heapq

# Heap Sort in descending order : '-' in, '-' out
def heapsort(iterable):
    h = []
    result = []
    # push in all items in the order
    for value in iterable:
        heapq.heappush(h, -value)

    # Pop out and append all items from the heap in the order they were pushed in
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)