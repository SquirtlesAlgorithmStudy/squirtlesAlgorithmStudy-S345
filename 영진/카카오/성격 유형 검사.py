def solution(survey, choices):
    answer = ''
    test={'R':0,'T':0,
          'C':0,'F':0,
          'J':0,'M':0,
          'A':0,'N':0}
    
    for i in range(len(survey)):
        if choices[i]>=5:
            test[survey[i][1]]+=choices[i]-4
        elif choices[i]<=3:
            test[survey[i][0]]+=4-choices[i]
    
    test_values=list(test.values())
    test_keys=list(test.keys())
    
    for i in range(0,7,2):
        if test_values[i]>=test_values[i+1]:
            answer+=test_keys[i]
        else:
            answer+=test_keys[i+1]
    return answer




"""
1.dictiionary: dic('key1':value1, 'key2':value2,,,,,)
2.dic.keys():dic의 key값들을 모두 리턴한다
3.dic.values():dic의 value값들을 모두 리턴한다
"""