# 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.

# 내 코드
select ins.ANIMAL_ID, ins.NAME
from animal_ins as ins
join (select ai.animal_id, (ao.datetime - ai.datetime) as term
     from animal_ins as ai
     join animal_outs as ao on ai.animal_id = ao.animal_id) join1
     on ins.animal_id = join1.animal_id
order by term desc
limit 2