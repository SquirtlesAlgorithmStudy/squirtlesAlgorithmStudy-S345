# 이 서비스에서는 공간을 둘 이상 등록한 사람을 "헤비 유저"라고 부릅니다. 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회하는 SQL문을 작성해주세요.

# 내 코드
select p1.ID, p1.NAME, p1.HOST_ID
from places as p1
join (select HOST_ID
     from places
     group by host_id
     having count(ID) >= 2) as p2 on p1.HOST_ID = p2.HOST_ID
order by ID
