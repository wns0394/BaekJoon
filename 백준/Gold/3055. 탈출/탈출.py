import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, sys.stdin.readline().split())

arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
visited = [[[0] * 2 for _ in range(c)] for _ in range(r)]
q = deque()

for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            # 물을 무조건 우선적으로 넣어야한다!!!
            q.appendleft((i, j, 0))
            visited[i][j][0] = 1
        elif arr[i][j] == 'S':
            q.append((i, j, 1))
            visited[i][j][1] = 1

while q:
    x, y, z = q.popleft()
    if arr[x][y] == 'D':
        print(visited[x][y][z] -1)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위안에 존재하고
        if 0 <= nx < r and 0 <= ny < c:
            # 다음칸이 비어 있고 고슴도치랑 물 둘다 방문한적 없다면
            if arr[nx][ny] == '.' and visited[nx][ny][0] == 0 and visited[nx][ny][1] == 0:
                q.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1
            # 고슴도치가 이동하고 다음이 비버라면
            if arr[nx][ny] == 'D' and z == 1:
                q.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1
else:
    print('KAKTUS')