import sys

input = sys.stdin.readline

# 나무의 수 n
# 집에 가져가려고 하는 나무의 길이 m
n, m = map(int, input().split())

# 나무의 길이들 arr
arr = list(map(int, input().split()))

arr.sort()

s = 1
e = arr[n - 1]


while s <= e:
    mid = (s+e) // 2

    result = 0

    for i in range(n):
        if arr[i] - mid > 0:
            result += arr[i] - mid

    if result >= m:
        s = mid + 1
    if result < m:
        e = mid - 1

print(e)

