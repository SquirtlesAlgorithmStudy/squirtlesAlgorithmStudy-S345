# 입양 못 간 동물 중 가장 오래 보호소에 있었던 동물 3마리 
-- 코드를 입력하세요
select ins.name, ins.datetime
from animal_ins as ins
left join animal_outs as outs on ins.animal_id = outs.animal_id
where outs.animal_id is null
order by ins.datetime asc
limit 3 # 세개만 출력

