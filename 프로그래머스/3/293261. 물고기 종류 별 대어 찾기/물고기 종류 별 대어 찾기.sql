-- 코드를 작성해주세요
SELECT A.ID AS ID,
    B.FISH_NAME AS FISH_NAME,
    A.LENGTH AS LENGTH
FROM FISH_INFO AS A JOIN FISH_NAME_INFO AS B
    ON A.FISH_TYPE = B.FISH_TYPE
WHERE (A.FISH_TYPE, A.LENGTH) IN (SELECT FISH_TYPE, MAX(LENGTH) 
                                FROM FISH_INFO 
                                WHERE LENGTH IS NOT NULL 
                                GROUP BY FISH_TYPE)
ORDER BY ID 
-- 7번 줄 같이 묶어주기 --