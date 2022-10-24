# 수학적으로 접근하기보단, 알고리즘적으로 접근하기
# 참고한 코드
# 설명의 A AA AAA AAAA AAAAA AAAAE AAAAO -> 보고 dfs 떠올리기
def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    answer = dict()
    num = 0
    
    def dfs(s):
        nonlocal num
        # key : 가능한 word, value : 순서
        answer[s] = num
        num += 1
        
        if len(s) == 5:
            return
        for vowel in vowels:
            dfs(s + vowel)
    
    dfs("")
    return answer[word]