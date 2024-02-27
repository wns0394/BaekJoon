import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

inf = int(1e9)

arr = [[inf] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    arr[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if arr[a][b] > c:
        arr[a][b] = c

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            arr[a][b] = min(arr[a][b], arr[a][i] + arr[i][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == inf:
            print(0, end=' ')
        else:
            print(arr[i][j], end=' ')
    print()
