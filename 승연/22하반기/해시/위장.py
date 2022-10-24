# 케이스 1번에서 시간초과 나는 코드 (길이가 30일 경우 조합으로 풀면 시간초과 발생)
# [의상 이름, 의상 카테고리]
# key : 의상 카테고리 value : 의상 이름
from itertools import combinations
def solution(clothes):
    count = 0
    closet = {}
    categories = []
    for a, b in clothes:
        categories.append(b)
        
    tmp = set(categories)
    categories = list(tmp)

    # key값 미리 만들어주기
    for key in categories:
        closet.setdefault(key, [])

    for cloth, cate in clothes:
        closet[cate].append(cloth)
    # 카테고리가 3개일 경우 -> 각각 하나씩(value값들의 합), 두카테고리(카테고리 조합, 각 value값 곱하기), 전체 카테고리(각 value값 곱하기)

    # 총 카테고리가 5일 경우 1 ~ 4
    for i in range(0, len(categories)):
        if i == 0:
            lis = sum(list(closet.values()), [])
            count += len(lis)
        else:
            for combi in combinations(categories, i+1):
                tmp = 1
                for k in combi:
                    tmp *= len(closet[k])
                count += tmp
    return count

# 시간초과 안나는 코드
# 하의 2개, 상의 3개가 있을 때
# *잘못된 풀이
# combinations으로 하의만 입을때, 상의만 입을때, 둘다 입을때 경우의 수를 구한다
# *맞는 풀이
# (하의 2개+안입은 경우) * (상의 2개 + 안입은 경우) = 3 * 4 = 12
# 그리고 전체에서 -1 (전부다 안입는 경우의 수를 뺀다)

def solution(clothes):
    answer = 1
    dic = dict()

    for cloth, Type in clothes:
        if(dic.get(Type) == None ):
            dic[Type] = [cloth]
            continue
        dic[Type].append(cloth)    

    for Type in dic:
        answer *= len(dic[Type]) + 1

    return answer - 1