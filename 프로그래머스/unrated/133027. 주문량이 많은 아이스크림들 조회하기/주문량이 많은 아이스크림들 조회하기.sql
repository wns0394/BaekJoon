-- 코드를 입력하세요
SELECT F.FLAVOR
FROM FIRST_HALF AS F
JOIN JULY AS J
ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY F.TOTAL_ORDER +SUM(J.TOTAL_ORDER) DESC
LIMIT 3

# SELECT * FROM FIRST_HALF
# UNION ALL
# SELECT * FROM JULY
# SHIPMENT_ID	FLAVOR	TOTAL_ORDER
# 104	caramel	2600
# 101	chocolate	3200
# 103	mint_chocolate	1700
# 106	peach	2450
# 109	strawberry	3100
# 102	vanilla	2800
# 105	white_chocolate	3100

# SHIPMENT_ID	FLAVOR	TOTAL_ORDER
# 101	chocolate	520
# 102	vanilla	560
# 103	mint_chocolate	400
# 104	caramel	460
# 105	white_chocolate	350
# 106	peach	500
# 109	strawberry	520
# 209	strawberry	220

# 카라멜  3060
# 초코 3720
# 민트 초코 2100
# 복숭아 2950
# 딸기  3840
# 바닐라 3360
# 화이트 초코 3450