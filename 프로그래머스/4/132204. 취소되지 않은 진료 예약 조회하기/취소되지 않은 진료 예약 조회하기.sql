-- 코드를 입력하세요
SELECT C.APNT_NO AS APNT_NO,
    A.PT_NAME AS PT_NAME,
    C.PT_NO AS PT_NO,
    B.MCDP_CD AS MCDP_CD,
    B.DR_NAME AS DR_NAME,
    C.APNT_YMD AS APNT_YMD
FROM (PATIENT AS A JOIN APPOINTMENT  AS C
     ON A.PT_NO = C.PT_NO) JOIN DOCTOR AS B
     ON B.DR_ID = C.MDDR_ID
WHERE YEAR(C.APNT_YMD) = 2022
    AND
    MONTH(C.APNT_YMD) = 4
    AND
    DAY(C.APNT_YMD) = 13
    AND
    C.APNT_CNCL_YN = 'N'
    AND
    C.MCDP_CD = 'CS'
ORDER BY 6