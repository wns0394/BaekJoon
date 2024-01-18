import sys

input = sys.stdin.readline

n = int(input())

d = []

for i in range(n):
    arr = list(map(int, input().split()))
    d.append(arr)

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            d[i][j] += d[i-1][j]
        elif j == i:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] += max(d[i-1][j-1], d[i-1][j])

print(max(d[-1]))