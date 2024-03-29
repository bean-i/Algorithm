SELECT D.AUTHOR_ID, D.AUTHOR_NAME, D.CATEGORY, SUM(D.TOTAL_SALES) TOTAL_SALES
FROM (
    SELECT C.AUTHOR_ID, C.AUTHOR_NAME, B.CATEGORY, B.PRICE*A.SALES TOTAL_SALES
    FROM (
        SELECT BOOK_ID, SUM(SALES) SALES
        FROM BOOK_SALES
        WHERE SALES_DATE LIKE '2022-01-%'
        GROUP BY BOOK_ID
    ) A JOIN BOOK B JOIN AUTHOR C
    ON A.BOOK_ID = B.BOOK_ID AND B.AUTHOR_ID = C.AUTHOR_ID
) D
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY D.AUTHOR_ID, D.CATEGORY DESC