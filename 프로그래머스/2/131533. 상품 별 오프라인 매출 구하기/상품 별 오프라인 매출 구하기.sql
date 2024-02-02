-- 코드를 입력하세요
SELECT A.PRODUCT_CODE, A.PRICE*B.SALES AS SALES
FROM PRODUCT A INNER JOIN (
    SELECT PRODUCT_ID, SUM(SALES_AMOUNT) SALES
    FROM OFFLINE_SALE
    GROUP BY PRODUCT_ID
) B ON A.PRODUCT_ID = B.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE
