# -- 코드를 입력하세요
# SELECT ANIMAL_OUTS.ANIMAL_ID,ANIMAL_OUTS.NAME
# FROM ANIMAL_OUTS
# LEFT JOIN ANIMAL_INS
# ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
# WHERE ANIMAL_INS.ANIMAL_ID IS NULL

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS AS O
LEFT JOIN ANIMAL_INS AS I
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID