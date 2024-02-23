SELECT A.CAR_ID, MAX(A.AVAILABILITY) AVAILABILITY
FROM (
    SELECT CAR_ID, CASE WHEN START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16' THEN '대여중'
    ELSE '대여 가능'
    END AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) A
GROUP BY A.CAR_ID
ORDER BY A.CAR_ID DESC


/*
CAR_ID  AVAILABILITY
30  대여 가능
29  대여중
28  대여중
27  대여중
26  대여중
25  대여중
24  대여중
23  대여중
22  대여중
21  대여 가능
20  대여중
19  대여중
18  대여중
17  대여중
16  대여중
15  대여 가능
13  대여 가능
12  대여중
11  대여중
10  대여 가능
9   대여중
8   대여중
7   대여중
6   대여중
5   대여중
4   대여중
3   대여 가능
2   대여중
1   대여 가능
*/