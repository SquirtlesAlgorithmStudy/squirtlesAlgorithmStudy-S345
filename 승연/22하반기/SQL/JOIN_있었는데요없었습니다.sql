# 보호 시작일보다 입양일이 더 빠른 동물
# animal_id 같은데 ins보다 outs테이블의 datetime이 더 빠른거 찾기
-- 코드를 입력하세요
select ins.animal_id, ins.name
from animal_ins as ins
inner join animal_outs as outs on ins.animal_id = outs.animal_id
where ins.datetime > outs.datetime
order by ins.datetime asc