import sys

input = sys.stdin.readline

from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

d = [arr[0]]

for i in range(n):
    if arr[i] > d[-1]:
        d.append(arr[i])
    else:
        idx = bisect_left(d,arr[i])
        d[idx] = arr[i]

print(len(d))