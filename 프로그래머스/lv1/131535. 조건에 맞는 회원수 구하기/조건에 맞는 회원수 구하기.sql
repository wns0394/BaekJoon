-- 코드를 입력하세요
SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE LEFT(JOINED,4) = 2021 AND AGE BETWEEN 20 AND 29;