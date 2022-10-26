select ins.ANIMAL_ID, ins.ANIMAL_TYPE, ins.NAME
from ANIMAL_INS as ins
left join ANIMAL_OUTS as outs
on ins.ANIMAL_ID = outs.ANIMAL_ID
where ins.SEX_UPON_INTAKE in ('Intact Male', 'Intact Female') and outs.SEX_UPON_OUTCOME in ('Spayed Female', 'Neutered Male')
order by ins.animal_id