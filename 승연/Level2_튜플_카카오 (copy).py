def solution(s):
    #입력받은 문자열을 2차원 리스트 형태로 변환
    s = s.split('},{')
    s[0] = s[0][2:]
    s[-1] = s[-1][:-2]
    for i in range(len(s)):  
        s[i] = list(map(int,s[i].split(',')))

    answer = []
    #2차원 리스트 요소의 길이 순으로 정렬
    s.sort(key=len)
    #idea : 두 번째 요소부터 (i번째 요소들) - (i-1번째 요소들) answer에 append
    for i in range(len(s)):
        if i ==0:
            answer.append(int(s[i][0]))
        else:
            i_sub_im1 = ([x for x in s[i][:] if x not in s[i - 1]][:])
            answer.append(i_sub_im1[0])
    
    return answer