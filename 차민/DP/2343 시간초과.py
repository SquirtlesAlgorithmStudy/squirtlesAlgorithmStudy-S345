#n = 강의 수, m= 블루레이 수
n, m = map(int, input().split())

#n개만큼의 강의 입력받기
arr = list(map(int, input().split()))

#시작점, 끝점
start = max(arr)
end = sum(arr)


#블루레이 수만큼. 원소는 블루레이 합
com = []
min_value = 0
def binary_search(array, start, end):
  sum = 0
  mid = (start + end)//2

  for j in range(n):
    if sum+array[j] < mid: 
      sum = sum+array[j]
    else :
      com.append(sum)
      sum = array[j]
      
  
  if len(com)>m : #블루레이개수가 m을 초과
    return binary_search(array,  mid, end)
  elif len(com)<m : #블루레이개수가 m보다 작을 때
    return binary_search(array,  start, mid)
  else : #블루레이개수가 m일 때 -> 하나씩 줄여나가면서 최솟값 찾기 

    while(1):
      mid = mid-1
      for j in range(n):
          if sum < mid: 
            sum = sum+arr[j]
          else :
            com.append(sum)
      if len(com) !=m:
        break

  return mid

  
result = binary_search(arr, start, end)
print(result)