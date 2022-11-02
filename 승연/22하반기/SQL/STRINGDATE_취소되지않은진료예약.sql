# PATIENT, DOCTOR 그리고 APPOINMENT 테이블에서 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성해주세요. 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력되도록 작성해주세요. 결과는 진료예약일시를 기준으로 오름차순 정렬해주세요.

# 여러 테이블을 가지고 결과를 낼 때는 반드시 JOIN 잊지 말기 !!!!!!
SELECT ap.APNT_NO, pat.PT_NAME, pat.PT_NO, ap.MCDP_CD, doc.DR_NAME, ap.APNT_YMD
from appointment as ap
join doctor as doc on ap.MDDR_ID = doc.DR_ID
join patient as pat on ap.PT_NO = pat.PT_NO
where year(APNT_YMD) = '2022' and month(APNT_YMD) = '04' and day(APNT_YMD) = '13'
and APNT_CNCL_YN = 'N' and ap.MCDP_CD = 'CS'
order by APNT_YMD asc
