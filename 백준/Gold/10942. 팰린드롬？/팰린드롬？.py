import sys

input = sys.stdin.readline

n = int(input())

arr = [0] + list(map(int, input().split()))

m = int(input())

d = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    d[i][i] = 1

for i in range(1,n):
    if arr[i] == arr[i+1]:
        d[i][i+1] = 1

for j in range(1,n+1):
    for i in range(1,n):
        if d[i+1][j-1] == 1 and arr[i] == arr[j]:
            d[i][j] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(d[s][e])
