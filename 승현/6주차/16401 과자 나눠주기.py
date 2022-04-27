import sys
fastin = sys.stdin.readline

#ㅇ아앙이읻드들듥고과 ㄱ고과ㅈ자작 ㄱ가갑값 ㅇ이입ㄹ려력
child, snacnt = map(int,fastin().split())

#ㄷㄷㅏㅏㄴㅊ체 ㅇ이입ㄹ려력
snacks = list(map(int,fastin().split()))


start = 0
end = max(snacks)

#ㅈ주줄줈수ㅅ ㅇ어업없ㅇ으을 ㄱ겨경ㅇ우 0ㅊ추출ㄹ려력
result = 0
while (start <= end):
  mid = (start+end) // 2
  cnt = 0

  if mid == 0:
    break
    
  for snack in snacks:
    cnt += snack // mid


  if cnt >= child:
    start = mid + 1
    result = mid
  else:
    end = mid - 1

print (result)