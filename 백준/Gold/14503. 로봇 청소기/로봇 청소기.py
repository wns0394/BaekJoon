from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global d
    q = deque()
    q.append((r, c, 1))
    visited[r][c] = 1
    while q:
        x, y, count = q.popleft()
        flag = 0
        # 먼저 회전 4번
        # 회전
        for _ in range(4):
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                # 지나갈수있고 가본적 없으면
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, count + 1))
                    flag = 1
                    break
        # 다회전했는데 청소할곳없다?
        # 후진
        if flag == 0:
            if arr[x-dx[d]][y-dy[d]] == 1:
                print(count)
                break
            else:
                q.append((x-dx[d],y-dy[d],count))


# 문제를 잘 읽자,,,,,,,,,
# 4칸중에 청소안된게 있으면 회전
# 가고 회전하는게 아니라 먼저 회전하고 간다
# 0 북↑, 1 동→, 2 남↓, 3 서←
# 0에서 3이 되어야 한다.
# 1에서 0이 되어야 한다.
# 2에서 1이 되어야 한다.
# 3에서 2가 되어야 한다
# (x+3) % 4
# 방크기 n,m
n, m = map(int, input().split())
# 시작지점
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
bfs()
