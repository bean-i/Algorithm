
SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, B.SCORE
FROM (
    SELECT *
    FROM REST_INFO
    WHERE ADDRESS LIKE '서울%'
) A JOIN (
    SELECT REST_ID, ROUND(AVG(REVIEW_SCORE), 2) SCORE
    FROM REST_REVIEW
    GROUP BY REST_ID
) B
ON A.REST_ID = B.REST_ID
ORDER BY SCORE DESC, A.FAVORITES DESC


# REST_ID	REST_NAME	FOOD_TYPE	FAVORITES	ADDRESS	SCORE
# 00001	은돼지식당	한식	734	서울특별시 중구 다산로 149	5.00
# 00002	하이가쯔네	일식	112	서울시 중구 신당동 375-21	4.50
# 00004	스시사카우스	일식	230	서울시 강남구 신사동 627-27	4.29
# 00003	따띠따띠뜨	양식	102	서울시 강남구 신사동 627-3 1F	4.00
