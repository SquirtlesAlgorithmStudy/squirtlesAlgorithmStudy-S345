# 답 참고
# count랑 sum헷갈리지 말자 !!!!!!!

# 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.
# first_half 의 key : flavor / shipment_id는 july의 외래키

select FLAVOR
from (select jul.flavor as FLAVOR, sum(jul.total_order)+sum(fh.total_order) as total_sales
from july as jul
left outer join first_half as fh on jul.flavor = fh.flavor
group by jul.flavor
order by total_sales desc) new_table
limit 3