import sys
from pprint import pprint
input = sys.stdin.readline

inf = int(1e9)

n, m = map(int, input().split())

arr = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    arr[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for a in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = min(arr[i][j], arr[i][a] + arr[a][j])


result = inf
x = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        count += arr[i][j]

    if result > count:
        result = count
        x = i
print(x)