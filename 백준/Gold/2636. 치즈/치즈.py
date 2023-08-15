from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    q = deque()
    # 가장자리는 치즈가 불가능하므로
    q.append((0,0))
    visited[0][0] = 1
    # 녹인 개수
    cnt = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 0이면 q에 넣어준다.
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                # 치즈라면 녹인다.
                elif arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    arr[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    last.append(cnt)
    return cnt


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

last = []
count = 0
while True:
    visited = [[0] * m for _ in range(n)]
    result = bfs()
    # 녹은 회수가 0개이면 끝난것이므로
    if result == 0:
        print(count)
        break
    count += 1
print(last[-2])