import sys

from pprint import pprint

input = sys.stdin.readline

n, a, d = map(int,input().split())

arr = list(map(int,input().split()))

count = 0

b = 0
for i in range(n):
    if arr[i] == a + d*b:
        count += 1
        b += 1

print(count)