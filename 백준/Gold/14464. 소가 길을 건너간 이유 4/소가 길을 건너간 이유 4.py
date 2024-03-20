import sys

input = sys.stdin.readline

c, n = map(int, input().split())

chicken = []

cow = []

for _ in range(c):
    t = int(input())
    chicken.append(t)

for _ in range(n):
    a, b = map(int, input().split())
    cow.append((a, b))

chicken.sort()
cow.sort(key=lambda x: (x[1], x[0]))

result = 0

vi = [0] * n

for i in range(c):
    for j in range(n):
        if cow[j][0] <= chicken[i] <= cow[j][1] and not vi[j]:
            result += 1
            vi[j] = 1
            break

print(result)
