import sys

input = sys.stdin.readline

from collections import deque

dx1 = [-1, 0, 1, 0]
dy1 = [0, 1, 0, -1]

dx2 = [-1, -1, -2, -2, 1, 1, 2, 2]
dy2 = [-2, 2, -1, 1, 2, -2, 1, -1]

dx3 = [-1, 0, 1, 0, -1, -1, -2, -2, 1, 1, 2, 2]
dy3 = [0, 1, 0, -1, -2, 2, -1, 1, 2, -2, 1, -1]
k = int(input())

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

q = deque()

q.append((0, 0, 0))
visited[0][0][0] = 1
flag = 1
while q:
    x, y, z = q.popleft()
    if x == n - 1 and y == m - 1:
        flag = 0
        print(visited[x][y][z] - 1)
        break
    if z < k:
        for i in range(12):
            nx = x + dx3[i]
            ny = y + dy3[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    if i <= 3 and visited[nx][ny][z] == 0:
                        q.append((nx, ny, z))
                        visited[nx][ny][z] = visited[x][y][z] + 1
                    elif i > 3 and visited[nx][ny][z+1] == 0:
                        q.append((nx, ny, z + 1))
                        visited[nx][ny][z + 1] = visited[x][y][z] + 1
    else:
        for i in range(4):
            nx = x + dx1[i]
            ny = y + dy1[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    q.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1

if flag:
    print(-1)
