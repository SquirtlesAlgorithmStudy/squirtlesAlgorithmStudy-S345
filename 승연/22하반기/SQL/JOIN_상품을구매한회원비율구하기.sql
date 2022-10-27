# 답 참고 (다시 풀어보기.....)

select year(os.sales_date) as YEAR, 
month(os.sales_date) as MONTH,
count(distinct os.user_id) as PUCHASED_USER,
round((count(distinct os.user_id)) / (select count(ui.user_id) from user_info as ui where year(ui.joined) = 2021), 1) as PUCHASED_RATIO
from online_sale as os
join user_info as ui on os.user_id = ui.user_id
where year(joined) = 2021
group by year, month
order by year, month

# 참고한 식
SELECT YEAR(O.SALES_DATE) AS YEAR
    , MONTH(O.SALES_DATE) AS MONTH
    , COUNT(DISTINCT O.USER_ID) AS PURCHASE_USERS
    , ROUND(COUNT(DISTINCT O.USER_ID)/ (
        SELECT COUNT(USER_ID)
        FROM USER_INFO
        WHERE YEAR(USER_INFO.JOINED) = 2021),
            1) AS PURCHASED_RATIO
FROM ONLINE_SALE O
JOIN USER_INFO U
ON U.USER_ID = O.USER_ID
WHERE YEAR(U.JOINED) = 2021
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH