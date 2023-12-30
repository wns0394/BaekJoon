import sys

input = sys.stdin.readline

n, q = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

for i in range(1,n):
    arr[i] += arr[i-1]


for _ in range(q):
    l, r = map(int, input().split())
    if l != 1:
        print(arr[r-1]-arr[l-2])
    else:
        print(arr[r-1])