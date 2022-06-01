import sys
input = sys.stdin.readline()

def solution(s):
    result=[]
    #문자열 길이가 1일 때 반환값 항상 1
    if len(s)==1:
        return 1
    #쪼갤 수 있는 최대 길이 : 문자열 길이의 반
    for i in range(1, (len(s)//2)+1):
        b = ''
        #문자열 연속으로 반복되는지 체크하는 변수
        cnt = 1
        tmp=s[:i]
        #i 만큼 문자 쪼개기
        for j in range(i, len(s), i):
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b = b + str(cnt)+tmp
                else:
                    b = b + tmp
                tmp=s[j:j+i]
                cnt = 1
        if cnt!=1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
                
        result.append(len(b))
    return min(result)