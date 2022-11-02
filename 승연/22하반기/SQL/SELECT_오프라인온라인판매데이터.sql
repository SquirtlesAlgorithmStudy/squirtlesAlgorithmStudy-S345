# ONLINE_SALE 테이블과 OFFLINE_SALE 테이블에서 2022년 3월의 오프라인/온라인 상품 판매 데이터의 판매 날짜, 상품ID, 유저ID, 판매량을 출력하는 SQL문을 작성해주세요. OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시해주세요. 결과는 판매일을 기준으로 오름차순 정렬해주시고 판매일이 같다면 상품 ID를 기준으로 오름차순, 상품ID까지 같다면 유저 ID를 기준으로 오름차순 정렬해주세요.

# 답 참고

# mysql에서 합집합 구할 때 union 사용 !!!
select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from online_sale
where year(sales_date) = '2022' and month(sales_date) = '03'
union 
# null as USER_ID : offline_sale 테이블에는 USER_ID열이 없기 때문에 null 열 생성해서 합침
select SALES_DATE, PRODUCT_ID, null as USER_ID, SALES_AMOUNT
from offline_sale
where year(sales_date) = '2022' and month(sales_date) = '03'
order by SALES_DATE asc, PRODUCT_ID asc, USER_ID asc
