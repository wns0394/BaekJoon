
t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    q = []
    q.append((x,y))
    arr[x][y] = 0

    while q:
        x,y = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    q.append((nx,ny))

for _ in range(t):
    m, n, k = map(int,input().split())
    arr = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int,input().split())
        arr[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i,j)
                count +=1
    print(count)