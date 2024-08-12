import sys

input = sys.stdin.readline
from copy import deepcopy
n, k = map(int, input().split())

result = list(map(int, input().split()))
d = list(map(int, input().split()))

count = 0

arr = [0] * n

while count < k:

    for i in range(n):
        arr[d[i]-1] = result[i]
    result = deepcopy(arr)

    count += 1

print(*arr)