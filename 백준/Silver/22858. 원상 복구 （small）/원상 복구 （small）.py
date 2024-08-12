import sys

input = sys.stdin.readline

n, k = map(int, input().split())

result = list(map(int, input().split()))
d = list(map(int, input().split()))

count = 0


while count < k:

    arr = [0] * n
    for i in range(n):
        arr[d[i]-1] = result[i]
    result = arr

    count += 1

print(*arr)