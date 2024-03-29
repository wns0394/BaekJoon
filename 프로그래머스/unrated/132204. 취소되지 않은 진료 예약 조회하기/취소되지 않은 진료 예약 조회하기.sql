SELECT A.APNT_NO, P.PT_NAME, P.PT_NO,  A.MCDP_CD, A.DR_NAME, A.APNT_YMD
FROM PATIENT AS P
JOIN (
    SELECT A.APNT_NO, A.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
    FROM APPOINTMENT AS A
    JOIN DOCTOR AS D 
    ON D.DR_ID = A.MDDR_ID
    WHERE A.MCDP_CD = 'CS' AND LEFT(APNT_YMD,10) = '2022-04-13' AND APNT_CNCL_YN = 'N'
) AS A
ON A.PT_NO = P.PT_NO
ORDER BY APNT_YMD