# ---- 구조 x
# |- -| 후 중간에 - 추가 가능 / |---|는 안됨

def append_situation (x, y, con, answer, n):
    #기둥
    if (con == 0):
        #기둥의 경우, 바닥 설치 or  밑에 기둥 or 
        if(y == 0 or ([x , y-1, 0] in answer) or ([x-1, y, 1] in answer) or([x,y,1] in answer)):
            return True
        else:
            return False
            
    if (con == 1):
        #보인 경우, n보다 커야한다 and 보 사이에 있는 경우 or 기둥위에 있는 경우 
        if (y > 0 and ([x-1,y,1] in answer and [x+1,y,1] in answer) or ([x,y-1,0] in answer) or ([x+1, y-1,0] in answer)):
            return True
        else:
            return False

def remove_situation (x, y, con, answer, n):
    #기둥 제거 안되는 경우
    if (con == 0):
        #ㅡ|,|ㅡ일경우
        if([x-1, y+1, 0] in answer or [x,y+1,(0 or 1) in answer]):
            #-|-인 경우는 삭제 가능
            if ([(x-1,y+1,0)] in answer and [x,y+1,(0 or 1)] in answer):
                return True
        return False
        
    #보 제거가 안되는 경우, 4개 이상 연속으로 배치될 경우(3개 ok), |-|
    if (con == 1): 
        if (#0u00
            ([x-2,y,1] in answer and [x-1,y,1] in answer and [x+1,y,1] in answer) or 
            #00u0
            ([x-1,y,1] in answer and [x+1,y,1] in answer and [x+2,y,1] in answer) or 
            #|ㄱ
            ([x,y-1,0] in answer and [x+1, y, 0] in answer) or 
            #ㄴ|
            ([x,y,0] in answer and [x+1, y-1, 0] in answer)):
            return False
        
def solution(n, build_frame):
    answer = []
    for build in build_frame:
        print("상태",answer)
        # 생성인 경우
        if (build[3] == 1):
            answer.append([build[0],build[1],build[2]])
            print("설치append",answer)
            if(append_situation(build[0],build[1],build[2], answer, n) ==  False):
                answer.remove([build[0],build[1],build[2]])
                print("설치remove",answer)
                #answer.append([build[0],build[1],build[2]])

        #삭제인 경우
        if (build[3] == 0):
            answer.remove([build[0], build[1], build[2]])
            print("삭제 값",[build[0], build[1], build[2]])
            print("삭제remove",answer)
            if (remove_situation(build[0],build[1], build[2],answer,n) == False):
                answer.append([build[0],build[1],build[2]])
                print("재설치 값",[build[0], build[1], build[2]])
                print("삭제append",answer)
            #print(answer)
            
    answer.sort()
    return answer
