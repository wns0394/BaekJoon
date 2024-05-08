import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# d[i] : i번째까지 가장 긴 감소하는 길이
d = [1] * n

d[0] = 1

for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            d[i] = max(d[i],d[j] + 1)

print(max(d))