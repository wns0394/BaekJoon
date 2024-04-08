import sys
input = sys.stdin.readline

n = int(input())

dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort()

s = dots[0][0]
e = dots[0][1]

result = e - s

for i in range(1, n):
    if dots[i][0] > e:
        s = dots[i][0]
    else:
        s = e
    if dots[i][1] > e:
        e = dots[i][1]
        result += e-s

print(result)
