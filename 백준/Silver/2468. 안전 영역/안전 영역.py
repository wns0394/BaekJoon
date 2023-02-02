
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y,a):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] > a and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1

n = int(input())

arr =[list(map(int,input().split())) for _ in range(n)]


max_height = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > max_height:
            max_height = arr[i][j]

result = 0
for a in range(max_height):
    count = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > a and visited[i][j] == 0:
                bfs(i,j,a)
                count += 1
    result = max(result, count)
print(result)