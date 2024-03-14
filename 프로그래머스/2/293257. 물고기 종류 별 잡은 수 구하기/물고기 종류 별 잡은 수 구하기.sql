-- 코드를 작성해주세요

SELECT COUNT(A.ID) AS FISH_COUNT,
    B.FISH_NAME AS FISH_NAME
FROM FISH_INFO AS A JOIN FISH_NAME_INFO AS B
    ON A.FISH_TYPE = B.FISH_TYPE
GROUP BY B.FISH_NAME
ORDER BY FISH_COUNT DESC