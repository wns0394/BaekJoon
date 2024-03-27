import sys

input = sys.stdin.readline

from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        x = q.popleft()

        for i in range(1, n + 1):
            if visited[i] == 0 and arr[x][i] == 1:
                q.append(i)
                visited[i] = visited[x] + 1
    return visited


n, m = map(int, input().split())

arr = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

result = int(1e9)
index = 0
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    count = sum(bfs(i)) - 5
    if result > count:
        result = count
        index = i

print(index)
