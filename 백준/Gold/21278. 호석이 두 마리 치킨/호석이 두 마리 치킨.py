import sys

input = sys.stdin.readline

n, m = map(int, input().split())

inf = int(1e9)

arr = [[inf] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(1, n + 1):
    arr[i][i] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

result = inf
x = 0
y = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        count = 0
        for c in range(1, n + 1):
            count += min(arr[c][i], arr[c][j]) * 2

        if count < result:
            result = count
            x = i
            y = j

print(x, y, result)
