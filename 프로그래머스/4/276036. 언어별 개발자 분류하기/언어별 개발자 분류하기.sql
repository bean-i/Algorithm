SELECT
    CASE
        WHEN EXISTS(
            SELECT S.CODE
            FROM SKILLCODES S
            WHERE A.SKILL_CODE & S.CODE = S.CODE AND S.NAME = 'Python'
        ) AND EXISTS(
            SELECT S.CODE
            FROM SKILLCODES S
            WHERE A.SKILL_CODE & S.CODE = S.CODE AND S.CATEGORY = 'Front End'
        ) THEN 'A'
        WHEN EXISTS(
            SELECT S.CODE
            FROM SKILLCODES S
            WHERE A.SKILL_CODE & S.CODE = S.CODE AND S.NAME = 'C#'
        ) THEN 'B'
        WHEN EXISTS(
            SELECT S.CODE
            FROM SKILLCODES S
            WHERE A.SKILL_CODE & S.CODE = S.CODE AND S.CATEGORY = 'Front End'
        ) THEN 'C'
        END GRADE, A.ID, A.EMAIL
FROM DEVELOPERS A
HAVING GRADE IS NOT NULL
ORDER BY GRADE, A.ID