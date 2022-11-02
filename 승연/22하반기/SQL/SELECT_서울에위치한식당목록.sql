# REST_INFO와 REST_REVIEW 테이블에서 서울에 위치한 식당들의 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회하는 SQL문을 작성해주세요. 이때 리뷰 평균점수는 소수점 세 번째 자리에서 반올림 해주시고 결과는 평균점수를 기준으로 내림차순 정렬해주시고, 평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬해주세요.

# where절 join 다음, order by 위에 넣어야 함. 이 부분 때문에 처음 오류

select ri.REST_ID, ri.REST_NAME, ri.FOOD_TYPE, ri.FAVORITES, ri.ADDRESS, SCORE
from rest_info as ri
join (select rest_id, round(sum(review_score)/count(*), 2) as SCORE
     from rest_review
     group by rest_id) join1 on ri.rest_id = join1.rest_id
where ri.address like '서울%'
order by SCORE desc, ri.FAVORITES desc