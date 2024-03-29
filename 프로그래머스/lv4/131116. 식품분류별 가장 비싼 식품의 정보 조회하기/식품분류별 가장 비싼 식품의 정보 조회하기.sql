SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME 
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (
    SELECT CATEGORY, MAX(PRICE) FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자','국','김치','식용유')
    GROUP BY CATEGORY
)
ORDER BY MAX_PRICE DESC

# SELECT * FROM  FOOD_PRODUCT WHERE CATEGORY IN ('과자','국','김치','식용유')

# PRODUCT_ID	PRODUCT_NAME	PRODUCT_CD	CATEGORY	PRICE

# P0014	맛있는마조유	CD_OL00004	식용유	8950
# P0051	맛있는배추김치	CD_KC00001	김치	19000
# P0074	맛있는김치찌개	CD_SU00004	국	2900
# P0093	맛있는허니버터칩	CD_CK00003	과자	1950