# MEMBER_PROFILE와 REST_REVIEW 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성해주세요. 회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 작성해주시고, 결과는 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬해주세요.

# 답 참고
# 시간 많이 걸렸던 문제 #

  
select member_name, review_text, date_format(review_date, '%Y-%m-%d') as review_date # 여기서 '22' 가 아닌 '2022'이렇게 출력하고 싶으면 Y대문자 !
from rest_review # 아래에 order by나 having절은 필요없음. 조인시 합계의 최댓값이랑 같은 member_id 걸러주기 때문에
inner join (
    select member_id as join1_member_id # 이렇게 조인할 때 키값 이름 따로 설정해주는거 !!, count(*) as count # 이부분 여러 번 다시 보기
    from rest_review
    group by member_id
    order by count desc
    limit 1
) join1 on rest_review.member_id = join1.join1_member_id
inner join (select member_name, member_id as join2_member_id # 조인시 키값 이름 따로 설정
            from member_profile) join2 on rest_review.member_id = join2.join2_member_id
order by review_date asc, review_text asc