from collections import deque

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


# 처음 출발지들에서 모두 출발하고 그이후 아이들을 출발해야하므로
# 첫 출발지 후보들을 모두 q에 담아준다.
def bfs():
    q = deque(queue)

    while q:
        z, x, y = q.popleft()
        visited[z][x][y] = 1

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if arr[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    q.append((nz, nx, ny))
                    visited[nz][nx][ny] = 1
                    arr[nz][nx][ny] = arr[z][x][y] + 1
        # print(arr)


m, n, h = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

visited = [[[0] * m for _ in range(n)] for _ in range(h)]
queue = []
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1 and visited[k][i][j] == 0:
                queue.append((k, i, j))

bfs()
max_count = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] > max_count:
                max_count = arr[k][i][j]
            # bfs끝나고 돌리는데 방문한적도 없고 토마토가 안익었으면
            elif arr[k][i][j] == 0 and visited[k][i][j] == 0:
                print(-1)
                exit()
# print(arr)
print(max_count-1)
