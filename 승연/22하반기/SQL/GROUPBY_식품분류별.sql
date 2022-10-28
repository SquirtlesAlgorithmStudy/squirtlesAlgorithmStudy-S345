# 답 참고
# FOOD_PRODUCT 테이블에서 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회하는 SQL문을 작성해주세요. 이때 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력시켜 주시고 결과는 식품 가격을 기준으로 내림차순 정렬해주세요.

# product_name 때문에 서브쿼리 필요

SELECT F.CATEGORY, F.PRICE AS MAX_PRICE, F.PRODUCT_NAME
FROM FOOD_PRODUCT AS F, (
    SELECT CATEGORY, MAX(PRICE) AS MPRICE
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY CATEGORY
) M
# 이부분 잘 보기 !! 조인 뿐만 아니라 이럴 때도 이렇게 쓸 수 있음
WHERE F.CATEGORY = M.CATEGORY AND F.PRICE = M.MPRICE
ORDER BY MAX_PRICE DESC;
