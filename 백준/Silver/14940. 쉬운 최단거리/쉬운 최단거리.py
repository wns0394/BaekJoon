import sys

input = sys.stdin.readline

from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]


visited = [[0]*m for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i,j))
            visited[i][j] = 1

while q:
    x,y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            print(visited[i][j] -1 , end=' ')
        else:
            if arr[i][j] == 1:
                print(-1, end=' ')
            else:
                print(visited[i][j], end=' ')
    print()