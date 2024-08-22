import sys

input = sys.stdin.readline

n = int(input())

d = [[0, 0] for _ in range(46)]

d[0] = [1, 0]

for i in range(1, 46):
    d[i][0] = d[i - 1][1]
    d[i][1] = d[i - 1][0] + d[i - 1][1]

print(*d[n])