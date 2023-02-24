import re

<<<<<<< HEAD
a = 4
=======
def solution(expression):
    cases = [['-','+','*'],['+','-','*'],['+','-','*'],['+','*','-'],['*','+','-'],['*','-','+']]
    num = re.split('[-|+|*]',expression)
    etc = re.split('[0|1|2|3|4|5|6|7|8|9]',expression)
    #num = re.split('([-|+|*])',expression) 으로 사용시 부호도 같이 num에 들어감
    etc = [i for i in etc if i not in '']
    ans_list = list()
            
    for ci in cases: #cases를 카운트
        for ei in range(len(etc)):
            print (ei)
            if (etc[ei] == ci[0]): 
                result = str(eval(num[ei]+etc[ei]+num[ei+1]))
                num.insert(ei,result)
                num.remove(num[ei])
                num.remove(ei+1)
               
                print('ei :', num[ei], 'ei+1 :', num[ei+1])
                
                
                print ('----결과',num, '\nei : ', ei,' ', etc[ei], '  ci : ', ci )
                
                #del num[ei+2]
                #print(num[ei])
                #del num[ei]
                """
                num.insert(int(num[ei+2]),result)
                num.pop(int(num[ei+1]))
                num.pop(int(etc[ei]))
                # num[ei] = result"""
                #print (num,'  ', etc, '\nei : ', ei,' ', etc[ei], '  ci : ', ci )
        """        
        for ei in range(len(etc)):
            if (etc[ei] == ci[1]): 
                result = eval(num[ei]+etc[ei]+num[ei+1])
                print (result,'  ', num, '\nei : ', ei,' ', etc[ei], '  ci : ', ci ) 
                num.insert(ei,result)
                print(num[ei])
                #del num[ei]
                #num.
                
                num.pop(num[ei])
                num.pop(num[ei+1])
                num.pop(etc[ei])
                num[ei] = str(result)
        for ei in range(len(etc)): 
            if (etc[ei] == ci[2]): 
                result = eval(num[ei]+etc[ei]+num[ei+1])
                print (result,'  ', num, '\nei : ', ei,' ', etc[ei], '  ci : ', ci )
                num.insert(ei,result)
                print(num[ei])
                #del num[ei]
                
                num.pop(num[ei])
                num.pop(num[ei+1])
                num.pop(etc[ei])
                num[ei] = str(result)
        #ans_list.append(num)
                
                #print (result,'  ', etc, '\nei : ', ei,' ', etc[ei], '  ci : ', ci ) 
    answer = 0#max(ans_list)
    return answer

#https://latte-is-horse.tistory.com/200"""
>>>>>>> adb74b8 ([의진] 임시)
