def solution(phone_book):
    n = len(phone_book)
    
    # 입력값이 문자형 숫자일 경우 그냥 sort를 하면
    # ex) "119", "97674223", "1195524421" -> "119", "1195524421", "97674223"로 정렬됨
    phone_book.sort()
    
    for i in range(n-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True