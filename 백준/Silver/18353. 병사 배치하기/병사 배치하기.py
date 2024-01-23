import sys

input = sys.stdin.readline

from bisect import bisect_left

n = int(input())

arr = list(map(int, input().split()))

new = list(reversed(arr))

# 감소하는 부분수열 만들기

d = [new[0]]

for i in range(n):
    if new[i] > d[-1]:
        d.append(new[i])
    else:
        idx = bisect_left(d, new[i])
        d[idx] = new[i]
    # print(d, i)
print(n-len(d))