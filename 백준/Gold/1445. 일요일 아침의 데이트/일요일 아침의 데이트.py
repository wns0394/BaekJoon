import sys

input = sys.stdin.readline

from collections import deque

# 아이디어
# s 출발지 f 도착지
# g 쓰레기 위치 . 깨끗한 칸
# s에서 f까지 가는데 쓰레기로 차 있는 칸을 되도록이면 적게 지나감
# 만약 되도록 적게 지나가는 경우의 수가 여러개라면
# 쓰레기 옆을 지나가는 칸의 개수를 최소로 해서 지나가려한다
# 칸이 비어있는데 인접한 칸에 쓰렉가 있다면 쓰레기 옆을 지나가는 것

# 일단 생각 visited 를 2차원으로 일단 만든다.
# visited[i][j] = (0,0)
# visited[i][[j][0] 은 i,j를 방문했을때 쓰레기 개수인지
# visited[i][[j][1] 은 i,j를 방문했을때 쓰레기 옆 개수인지

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

inf = int(1e9)

arr = [list(input().rstrip()) for _ in range(n)]

visited = [[[inf, inf] for _ in range(m)] for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            q.append((i, j, 0, 0))
            visited[i][j] = [0, 0]
        if arr[i][j] == 'g':
            if 0 <= i + 1 < n and arr[i + 1][j] == '.':
                arr[i + 1][j] = 'h'
            if 0 <= j - 1 < m and arr[i][j - 1] == '.':
                arr[i][j - 1] = 'h'
            if 0 <= i - 1 < n and arr[i - 1][j] == '.':
                arr[i - 1][j] = 'h'
            if 0 <= j + 1 < m and arr[i][j + 1] == '.':
                arr[i][j + 1] = 'h'
        if arr[i][j] == 'F':
            xe = i
            ye = j


while q:
    x, y, t, s = q.popleft()

    if x == xe and y == ye:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 'F':
                if visited[nx][ny][0] > t:
                    q.append((nx, ny, t, s))
                    visited[nx][ny] = [t, s]
                if visited[nx][ny][0] == t:
                    if visited[nx][ny][1] > s:
                        q.append((nx, ny, t, s))
                        visited[nx][ny] = [t, s]

            if arr[nx][ny] == '.':
                if visited[nx][ny][0] > t:
                    q.append((nx, ny, t, s))
                    visited[nx][ny][0] = t
                    visited[nx][ny][1] = s

                elif visited[nx][ny][0] == t:
                    if visited[nx][ny][1] > s:
                        q.append((nx, ny, t, s))
                        visited[nx][ny][0] = t
                        visited[nx][ny][1] = s

            if arr[nx][ny] == 'g':
                if visited[nx][ny][0] > t + 1:
                    q.append((nx, ny, t + 1, s))
                    visited[nx][ny][0] = t + 1
                    visited[nx][ny][1] = s
                elif visited[nx][ny][0] == t + 1:
                    if visited[nx][ny][1] > s:
                        q.append((nx, ny, t + 1, s))
                        visited[nx][ny][0] = t + 1
                        visited[nx][ny][1] = s

            if arr[nx][ny] == 'h':
                if visited[nx][ny][0] > t:
                    q.append((nx, ny, t, s+1))
                    visited[nx][ny][0] = t
                    visited[nx][ny][1] = s+1

                elif visited[nx][ny][0] == t:
                    if visited[nx][ny][1] > s+1:
                        q.append((nx, ny, t, s+1))
                        visited[nx][ny][0] = t
                        visited[nx][ny][1] = s+1

print(*visited[xe][ye])