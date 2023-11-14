from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y,z):
    q = deque()
    q.append((x,y,z))
    visited[x][y] = 1

    while q:
        x,y,z = q.popleft()
        if x == n-1 and y == n-1:
            return z
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.appendleft((nx,ny,z))
                    visited[nx][ny] = 1
                elif arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx,ny,z+1))
                    visited[nx][ny] = 1

n = int(input())

arr = [list(map(int,input())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

result = bfs(0,0,0)
print(result)