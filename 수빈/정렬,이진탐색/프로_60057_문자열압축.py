
def solution(s):
    length = len(s)
    minlen = length
    str1, str2 = "",""
    
    # 가능한 단위 범위 만큼 반복
    for unit in range(1, int(length/2)+1):
        tmplen = 0 # 해당 단위에서 길이를 저장하는 변수
        num = 1 # 같은 갯수를 세는 변수
        cur = 0 # 커서
        while cur<length:
            str1 = s[cur:cur+unit]
            str2 = s[cur+unit:cur+(2*unit)]
            # str1, str2에 단위만큼 잘라줌
            if str1==str2:
            # 만약 같다면 다음 문자에도 같을 확률이 있으니 num+=1 해준 후 넘어감
                num +=1
            else:
            # 다르다면 문자열에 추가 시켜줌
                if num==1: #만약 num이 1이면 =>이전에 같은 문자열이 없어서 압축시킬 필요가 없으니
                    tmplen +=len(str1)
                else:      #만약 num이 1보다 크다면 =>이전에 같은 문자열이 있어서 압축이 필요하니
                    tmplen +=len(str(num))   #num의 자릿수를 고려하기 위해 len(str(num))을 더해준 후
                    tmplen +=len(str1)        #해당 문자열(str1)의 길이를 더해준다
                    num =1
            cur +=unit
        #작은 길이를 저장
        minlen = min(minlen, tmplen)
    return minlen
        