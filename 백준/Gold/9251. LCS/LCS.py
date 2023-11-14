a = list(map(str, input()))
b = list(map(str, input()))
x = len(a)
y = len(b)

d = [[0] * (y + 1) for _ in range(x + 1)]


for i in range(1,x+1):
    for j in range(1,y+1):
        if a[i-1] == b[j-1]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[-1][-1])
