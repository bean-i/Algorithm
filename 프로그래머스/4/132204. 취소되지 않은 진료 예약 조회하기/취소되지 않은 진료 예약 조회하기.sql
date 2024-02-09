
SELECT A.APNT_NO, C.PT_NAME, C.PT_NO, A.MCDP_CD, B.DR_NAME, A.APNT_YMD
FROM APPOINTMENT A INNER JOIN DOCTOR B INNER JOIN PATIENT C
ON A.MDDR_ID = B.DR_ID AND A.PT_NO = C.PT_NO
WHERE APNT_YMD LIKE '2022-04-13%' AND APNT_CNCL_YN = 'N'
ORDER BY A.APNT_YMD