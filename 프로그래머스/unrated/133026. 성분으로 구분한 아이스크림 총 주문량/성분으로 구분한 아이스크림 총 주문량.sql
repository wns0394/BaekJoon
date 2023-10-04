# SELECT * FROM FIRST_HALF
# SHIPMENT_ID	FLAVOR	TOTAL_ORDER
# 104	caramel	2600
# 101	chocolate	3200
# 103	mint_chocolate	1700
# 106	peach	2450
# 109	strawberry	3100
# 102	vanilla	2800
# 105	white_chocolate	3100

# SELECT * FROM ICECREAM_INFO

# FLAVOR	INGREDIENT_TYPE
# caramel	sugar_based
# chocolate	sugar_based
# mint_chocolate	sugar_based
# peach	fruit_based
# strawberry	fruit_based
# vanilla	sugar_based
# white_chocolate	sugar_based

SELECT I.INGREDIENT_TYPE, SUM(F.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF AS F
JOIN ICECREAM_INFO AS I
ON F.FLAVOR = I.FLAVOR
GROUP BY I.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER