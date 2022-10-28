# 답 참고, 다시 봐야함
# 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

WITH RECURSIVE TIME AS(
SELECT 0 AS H UNION ALL SELECT H+1 FROM TIME WHERE H < 23
)
SELECT
H AS 'HOUR',
COUNT(HOUR(DATETIME)) AS 'COUNT'
FROM TIME LEFT JOIN ANIMAL_OUTS ON (H=HOUR(DATETIME))
GROUP BY H;