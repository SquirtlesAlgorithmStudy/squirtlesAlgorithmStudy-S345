import sys
input = sys.stdin.readline

N=int(input())

def recursive_fuction(i):
    if i==0:
        return print("_"*4*(N-i)+'"재귀함수가 뭔가요?"'
            +"\n"+"_"*4*(N-i)+'"재귀함수는 자기 자신을 호출하는 함수라네"'
            +"\n"+"_"*4*(N-i)+'라고 답변하였지.')
    else :
        print("_"*4*(N-i)+'"재귀함수가 뭔가요?"'
            +"\n"+"_"*4*(N-i)+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
            +"\n"+"_"*4*(N-i)+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
            +"\n"+"_"*4*(N-i)+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')      
        recursive_fuction(i-1)
        print("_"*4*(N-i)+'라고 답변하였지.')

recursive_fuction(N)