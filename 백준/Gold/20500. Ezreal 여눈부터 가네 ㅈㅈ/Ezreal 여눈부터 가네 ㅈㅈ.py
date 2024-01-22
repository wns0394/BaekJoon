import sys

input = sys.stdin.readline

n = int(input())

d = [0] * (n+1)

for i in range(2,n+1):
    if i % 2 == 0:
        d[i] = (d[i-1] * 2 + 1) % 1000000007
    else:
        d[i] = (d[i-1] * 2 - 1) % 1000000007

print(d[-1])