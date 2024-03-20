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

visited = [0] * c

for a, b in cow:
    for i in range(c):
        if a <= chicken[i] <= b and not visited[i]:
            result += 1
            visited[i] = 1
            break

print(result)
