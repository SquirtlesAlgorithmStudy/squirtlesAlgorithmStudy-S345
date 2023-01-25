N,M=map(int,input().split())
ans=[]

def back():
    if len(ans)==M:
        print(" ".join(map(str,ans)))
        return
    for i in range(1,N+1):
        ans.append(i)
        back()
        ans.pop()

back()

"""
1. ".join(리스트): ['a','b','c']의 리스트 'abc'로 출력
   '구분자'.join(리스트): 리스틔의 값과 값 사이에 '구분자'에 들어온 구분자를
   넣어서 하나의 문자열로 합쳐줌
"""