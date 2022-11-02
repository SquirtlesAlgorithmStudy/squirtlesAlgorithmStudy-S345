# 데이터 분석 팀에서는 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니가 있는지 알아보려 합니다. 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.

# 내 코드
select distinct cp1.CART_ID as CART_ID
from cart_products as cp1
join (select cart_id
     from cart_products
     where name = 'Milk') cp2 on cp1.cart_id = cp2.cart_id
where cp1.name = 'Yogurt'
order by cp1.CART_ID;

# 다른사람 코드 (굿!)
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME='MILK' AND CART_ID IN (SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME ="YOGURT") ;
