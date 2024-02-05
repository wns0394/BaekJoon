import sys

input = sys.stdin.readline

n = int(input())

d = [3,7]

for i in range(2,n):
    d.append((d[i-1]*2 + d[i-2])%9901)
print(d[n-1])