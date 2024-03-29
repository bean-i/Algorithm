/*
SELECT C.HISTORY_ID, CASE WHEN C.TYPE IS NULL THEN C.DAILY_FEE*C.DAY
ELSE ROUND(C.DAILY_FEE*C.DAY*(1 - D.DISCOUNT_RATE/100))
END FEE
FROM (
SELECT A.HISTORY_ID, B.CAR_TYPE, B.DAILY_FEE, DATEDIFF(A.END_DATE, A.START_DATE) + 1 AS DAY, CASE WHEN DATEDIFF(A.END_DATE, A.START_DATE) + 1 < 7 THEN NULL
    WHEN DATEDIFF(A.END_DATE, A.START_DATE) + 1 < 30 THEN '7일 이상'
    WHEN DATEDIFF(A.END_DATE, A.START_DATE) + 1 < 90 THEN '30일 이상'
    ELSE '90일 이상'
    END TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A JOIN CAR_RENTAL_COMPANY_CAR B
ON A.CAR_ID = B.CAR_ID
WHERE B.CAR_TYPE = '트럭'
ORDER BY A.HISTORY_ID
) C JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
ON C.CAR_TYPE = D.CAR_TYPE AND C.TYPE = D.DURATION_TYPE
ORDER BY FEE DESC, C.HISTORY_ID DESC
*/
# SELECT *
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# ORDER BY HISTORY_ID DESC

SELECT C.HISTORY_ID, CASE WHEN C.TYPE IS NULL THEN C.DAILY_FEE*C.DAY
ELSE ROUND(C.DAILY_FEE*C.DAY*(1 - D.DISCOUNT_RATE/100))
END FEE
FROM (
SELECT A.HISTORY_ID, B.CAR_TYPE, B.DAILY_FEE, DATEDIFF(A.END_DATE, A.START_DATE) + 1 AS DAY, CASE WHEN DATEDIFF(A.END_DATE, A.START_DATE) + 1 < 7 THEN NULL
    WHEN DATEDIFF(A.END_DATE, A.START_DATE) + 1 < 30 THEN '7일 이상'
    WHEN DATEDIFF(A.END_DATE, A.START_DATE) + 1 < 90 THEN '30일 이상'
    ELSE '90일 이상'
    END TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A JOIN CAR_RENTAL_COMPANY_CAR B
ON A.CAR_ID = B.CAR_ID
WHERE B.CAR_TYPE = '트럭'
ORDER BY A.HISTORY_ID
) C LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
ON C.CAR_TYPE = D.CAR_TYPE AND C.TYPE = D.DURATION_TYPE
ORDER BY FEE DESC, C.HISTORY_ID DESC
/*
history_id  FEE
724 6336960
681 5356240
630 4791360
558 4404960
653 3793160
722 2909040
594 1888600
680 1524750
714 1118150
591 1118150
556 813200
610 672000
676 568000
527 535000
720 532000
710 532000
701 504000
640 428000
641 426000
628 426000
623 336000
602 336000
673 321000
631 321000
654 284000
618 214000
586 214000
581 214000
546 214000
716 140000
711 107000
705 107000
627 107000
524 107000
*/