# 답 참고

# FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요. 이때 결과는 총매출을 기준으로 내림차순 정렬해주시고 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요.


-- 코드를 입력하세요
select fp.product_id as product_id, fp.product_name as product_name, fp.PRICE*join1.amount as total_sales
from food_product as fp
join (select product_id, sum(amount) as amount
      from food_order
      where PRODUCE_DATE between '2022-05-01' and '2022-05-31'
      group by product_id
     ) join1 on fp.product_id = join1.product_id
order by total_sales desc, product_id asc