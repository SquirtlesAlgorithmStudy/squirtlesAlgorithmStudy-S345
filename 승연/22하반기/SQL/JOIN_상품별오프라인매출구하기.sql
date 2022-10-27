# PRODUCT, OFFLINE_SALE 테이블 키 PRODUCT_ID
# 
-- 코드를 입력하세요
SELECT PRODUCT_CODE, price*sum(sales_amount) as SALES
from product as pr
join offline_sale as off on pr.product_id = off.product_id
group by product_code
order by sales desc, product_code asc