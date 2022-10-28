-- 코드를 입력하세요
SELECT table1.FOOD_TYPE, table1.REST_ID, table1.REST_NAME, table1.FAVORITES
from rest_info as table1, (select food_type, max(favorites) as mfavorite
                           from rest_info
                           group by food_type) as table2
where table1.food_type = table2.food_type and table1.favorites = table2.mfavorite
order by food_type desc