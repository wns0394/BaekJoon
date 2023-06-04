n, r, c = map(int, input().split())

result = 0
while n !=0:
    # 1사분면
    if 0 <= r <= (2 ** n // 2) - 1 and 0 <= c <= (2 ** n // 2) - 1:
        result += 0
    # 2사분면
    elif 0 <= r <= (2 ** n // 2) - 1 and (2 ** n // 2) - 1 < c:
        c = c - (2 ** n // 2)
        result += (2 ** n // 2) * (2 ** n // 2)
    # 3사분면
    elif (2 ** n // 2) - 1 < r and 0 <= c <= (2 ** n // 2) - 1:
        r = r - (2 ** n // 2)
        result += (2 ** n // 2) * (2 ** n // 2) * 2
    # 4사분면
    else:
        r = r - (2 ** n // 2)
        c = c - (2 ** n // 2)
        result += (2 ** n // 2) * (2 ** n // 2) * 3
    n -= 1

print(result)