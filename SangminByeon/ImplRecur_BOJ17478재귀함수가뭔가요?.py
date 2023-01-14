from sys import stdin

def chatBot(n,i=0):
    
    str1 = ""
    for _ in range(i):
        str1 = str1 + "____"
    str2 = ""
    for _ in range(i+1):
        str2 = str2 + "____"

    if n==0: 
        print(str1 + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        return
    
    print(str1 + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    print(str1 + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print(str1 + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    print(str2 + "\"재귀함수가 뭔가요?\"")
    chatBot(n-1,i+1)
    print(str2 + "라고 답변하였지.")
    

n = int(stdin.readline().rstrip())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
print("\"재귀함수가 뭔가요?\"")
chatBot(n)
print("라고 답변하였지.")