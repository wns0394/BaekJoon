import sys
from collections import deque

# 8방향
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == '.':
            q.append((i,j))

visited = [[0]*m for _ in range(n)]

# 파도를 다 검사 할 동안
while q:
    x,y = q.popleft()


    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] != '.':
                arr[nx][ny] = int(arr[nx][ny]) - 1
                if int(arr[nx][ny]) == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

result = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] > result:
            result = visited[i][j]
print(result)