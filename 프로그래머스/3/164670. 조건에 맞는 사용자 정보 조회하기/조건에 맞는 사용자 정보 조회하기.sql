SELECT B.USER_ID, B.NICKNAME, CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소', CONCAT(LEFT(TLNO, 3), '-', SUBSTRING(TLNO, 4, 4), '-', RIGHT(TLNO, 4)) AS '전화번호'
FROM (
    SELECT *
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING COUNT(*) >= 3
) A JOIN USED_GOODS_USER B
ON A.WRITER_ID = B.USER_ID
ORDER BY B.USER_ID DESC