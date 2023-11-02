t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    d = [[int(i+1) for i in range(n)]  for _ in range(k+1)]

    for i in range(1,k+1):
        for j in range(1,n):
            d[i][j] = sum(d[i-1][:j+1])
    print(d[k][n-1])