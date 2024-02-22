
SELECT A.FOOD_TYPE, A.REST_ID, A.REST_NAME, A.FAVORITES
FROM REST_INFO A INNER JOIN (
    SELECT REST_NAME, REST_ID, FOOD_TYPE, MAX(FAVORITES) FAVORITES
    FROM REST_INFO
    GROUP BY FOOD_TYPE
    ORDER BY FAVORITES DESC
) B ON A.FAVORITES = B.FAVORITES AND A.FOOD_TYPE = B.FOOD_TYPE
GROUP BY FOOD_TYPE
ORDER BY A.FOOD_TYPE DESC


# 애플우스	분식	15340	151
# 따띠따띠뜨	양식	1234023	102
# 스시사카우스	일식	1522074	230
# 만정	중식	12340	20
# 은돼지식당	한식	1150345	734