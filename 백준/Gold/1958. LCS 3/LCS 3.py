import sys

input = sys.stdin.readline

a = list(input().rstrip())
b = list(input().rstrip())
c = list(input().rstrip())

x = len(a)
y = len(b)
z = len(c)

d = [[[0] * (z + 1) for _ in range(y + 1)] for _ in range(x + 1)]

for i in range(1, x + 1):
    for j in range(1, y + 1):
        for k in range(1, z + 1):
            if a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]:
                d[i][j][k] = d[i - 1][j - 1][k - 1] + 1
            else:
                d[i][j][k] = max(d[i - 1][j][k], d[i][j - 1][k], d[i][j][k - 1])

print(d[-1][-1][-1])
