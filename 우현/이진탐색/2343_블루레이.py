N, M = map(int, input().split())
arr = list(map(int, input().split()))

lesson_total = sum(arr)
left, right = lesson_total // M, sum(arr)

answer = right
while left <= right:
  mid = (left + right) // 2

  if mid < max(arr):
    left = mid + 1
    continue
        
  count, temp = 0, 0
  for i in range(len(arr)):
    if arr[i] > mid:
      break
    elif temp + arr[i] <= mid:
      temp += arr[i]
    else:
      temp = arr[i]
      count += 1

  if count <= M - 1:  
    right = mid - 1
    answer = min(answer, mid)  
  else:  
    left = mid + 1

print(answer)