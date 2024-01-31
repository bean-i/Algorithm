-- 코드를 입력하세요

SELECT A.MCDP_CD AS "진료과코드", COUNT(*) AS "5월예약건수"
FROM (
    SELECT *
    FROM APPOINTMENT
    WHERE APNT_YMD LIKE '2022-05-%'
) A
GROUP BY A.MCDP_CD
ORDER BY COUNT(*), A.MCDP_CD