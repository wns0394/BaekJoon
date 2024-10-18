import sys

from pprint import pprint

from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append((x, 0))
    visited = [0] * (n + 1)

    while q:
        now, distance = q.popleft()

        if now == y:
            print(distance)
            break

        for next, dist in arr[now]:
            if visited[next] == 0:
                visited[next] = 1
                q.append((next, distance + dist))


n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, d = map(int, input().split())
    arr[a].append((b, d))
    arr[b].append((a, d))

for _ in range(m):
    x, y = map(int, input().split())
    bfs(x, y)
