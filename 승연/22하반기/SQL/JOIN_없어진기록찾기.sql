# 입양 기록은 있는데 보호소에 들어온 기록이 없는 동물 (outer join 오른쪽에 outs, ins is null)
-- 코드를 입력하세요

select outs.animal_id, outs.name
from animal_ins as ins
right join animal_outs as outs on ins.animal_id = outs.animal_id
where ins.animal_id is null
order by outs.animal_id