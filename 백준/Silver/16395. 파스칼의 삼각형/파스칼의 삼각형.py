import sys

input = sys.stdin.readline

n, m = map(int, input().split())

d = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 and j == 1:
            d[i][j] = 1
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j]

print(d[n][m])