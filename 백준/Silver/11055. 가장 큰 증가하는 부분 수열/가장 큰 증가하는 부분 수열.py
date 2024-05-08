import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

d = [0] * n
d[0] = arr[0]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j] + arr[i])
        else:
            d[i] = max(d[i],arr[i])

print(max(d))
