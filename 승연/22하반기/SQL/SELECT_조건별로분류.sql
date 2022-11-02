# FOOD_ORDER 테이블에서 5월 1일을 기준으로 주문 ID, 제품 ID, 출고일자, 출고여부를 조회하는 SQL문을 작성해주세요. 출고여부는 5월 1일까지 출고완료로 이 후 날짜는 출고 대기로 미정이면 출고미정으로 출력해주시고, 결과는 주문 ID를 기준으로 오름차순 정렬해주세요.

# 답 참고 !!
# case   when-then when-then else   end as 부분 잘 익히기!!!

select ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, '%Y-%m-%d') as OUT_DATE,
case
when OUT_DATE <= '2022-05-01' then "출고완료"
when OUT_DATE > '2022-05-01' then "출고대기"
else "출고미정"
end as 출고여부
from food_order;