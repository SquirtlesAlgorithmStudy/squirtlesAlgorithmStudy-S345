# ---- 구조 x
# |- -| 후 중간에 - 추가 가능 / |---|는 안됨

def situation (x, y, con, answer, n):
    if (x < n and y < n):
        #보인 경우
        if (con == 1):
            if(y == 0 or [x , y-1,(0 or 1)] in answer or [x-1, y,(0 or 1)] in answer):
                return True
            else:
                return False
            
        if (con == 0):
            if( y > 0 and (([x-1,y] in answer == True and [x+1,y] in answer == True) or ([x,y-1] in answer == True))):
                return True
            else:
                return False

            
            
def solution(n, build_frame):
    answer = []
    for build in build_frame:
        # 생성인 경우
        if (build[3] == 1):
            if (situation(build[0],build[1],build[2], answer, n) == True:
                answer.append([build[0],build[1],build[2]])
        
        #삭제인 경우
        if (build[3] == 0):
            answer.remove([build[0], build[1], build[2]])
            if (situation(build[0],build[1], build[2],answer,n) == False):
                answer.append([build[0],build[1],build[2]])                
            

    return answer
