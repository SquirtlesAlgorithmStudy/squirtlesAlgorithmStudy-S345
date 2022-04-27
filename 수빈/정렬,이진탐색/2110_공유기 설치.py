import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = [ int(input()) for _ in range(n)]
x.sort()

def binary():
    start = 1
    end = max(x)-1
    
    while start<=end:
        mid = (start+end)//2
        print('초기 mid', mid)
        
        cnt = 1
        wifi = min(x)+mid
        print('초기 wifi ', wifi)
        
        for i in range(1, len(x)):
            if wifi <=x[i]:
                cnt +=1
                wifi = x[i]+mid
                print('cnt ', cnt, '수정된 wifi ', wifi)
                
        if cnt >=c:
            start = mid +1
            print('if문 거침 ', start)
        else:
            end = mid-1
            print('else문 거침 ', end)
            
    return end

print(binary())

# cnt와 wifi(설치) 를 따로 세어줬고
# 조건이 되는 장치들을 for문, if문, while 문에 나눠서 걸어줌