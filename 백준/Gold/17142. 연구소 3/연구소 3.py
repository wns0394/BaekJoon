import sys

input = sys.stdin.readline

from itertools import combinations
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

q = deque()
virus = []
wall = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i, j))
        if arr[i][j] == 1:
            wall.append((i, j))

allcase = list(combinations(virus, m))
inf = int(1e9)
result = inf
for case in allcase:
    flag = True
    q = deque(case)
    visited = [[0] * n for _ in range(n)]
    for c in case:
        visited[c[0]][c[1]] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                # 비활성화된 바이러스
                if arr[nx][ny] == 2 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    max_count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and arr[i][j] == 0:
                flag = False
            if visited[i][j] > 0 and visited[i][j] > max_count and arr[i][j] == 0:
                max_count = visited[i][j]
        if flag == False:
            break
    if flag:
        result = min(result,max_count)
    # print(result)?

if result == inf:
    print(-1)
else:
    if result == 0:
        print(0)
    else:
        print(result-1)