import sys

from pprint import pprint

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    t = int(input())
    arr.append(t)

s = 0
e = max(arr) * m
reuslt = 0
while s <= e:
    mid = (s+e) // 2
    count = 0
    for i in arr:
        count += mid // i
    if count >= m:
        e = mid - 1
        result = mid
    else:
        s = mid + 1
print(result)