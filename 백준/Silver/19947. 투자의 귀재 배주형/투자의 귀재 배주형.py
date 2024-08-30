import sys

input = sys.stdin.readline

n, m = map(int, input().split())

d = [0] * (m + 1)

d[0] = n
if m > 0:
    d[1] = int(d[0] * 1.05)
if m > 1:
    d[2] = int(d[1] * 1.05)
if m > 2:
    d[3] = int(max(d[2] * 1.05, d[0] * 1.2))
if m > 3:
    d[4] = int(max(d[3] * 1.05, d[1] * 1.2))
if m > 4:
    for i in range(5, m + 1):
        d[i] = int(max(d[i - 1] * 1.05, d[i - 3] * 1.2, d[i - 5] * 1.35))

print(d[m])