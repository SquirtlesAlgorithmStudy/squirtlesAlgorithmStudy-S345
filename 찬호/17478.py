start ="어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
question = '"재귀함수가 뭔가요?"'
sentence2 ='"재귀함수는 자기 자신을 호출하는 함수라네"' 
sentence3 ="라고 답변하였지."
def rec(m):
    print("_"*(4*(n-m))+question)
    if not m:
        print("_"*(4*(n-m))+sentence2)
        print("_"*(4*(n-m))+sentence3)
        return
            
    print("_"*(4*(n-m))+"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\"")
    print("_"*(4*(n-m))+"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print("_"*(4*(n-m))+"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    rec(m-1)
    print("_"*(4*(n-m))+sentence3)


n = int(input())
print(start)
rec(n)

#알고리즘은 맞았는데 . 같은 사소한 걸 못 고쳐서 틀림 
#n차 
    
    
