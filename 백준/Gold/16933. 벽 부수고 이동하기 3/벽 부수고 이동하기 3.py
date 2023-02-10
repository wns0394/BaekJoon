
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


n, m, k = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

# 시작지점 0,0 얼마나 부셨는지 w 낮 :1 밤은 : -1로 지정할거임 마지막은 cnt
q = deque()
# x,y 좌표랑 w: 얼마나 부셨는지 s:낮인지 밤인지 판단하기위해
q.append((0,0,0,1,1))
visited[0][0][0] = 1

while q:
    x, y, w, s, c = q.popleft()

    if x == n - 1 and y == m - 1:
        print(c)
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            # 방문한적없고 이동가능하면
            if arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
                q.append((nx, ny, w, -s, c + 1))
                visited[nx][ny][w] = 1

            # 벽이고 방문한적없고 부신횟수가 k보다 작다면? 한번더 조사 -> 낮인지 밤인지
            elif arr[nx][ny] == 1 and w < k and visited[nx][ny][w + 1] == 0:
                # 밤이다? -> 부실수없다 그자리에서 한번 기다리자
                if s == -1:
                    # 저번위치 그대로 넣어주고 부신횟수도 그대로 밤낮만 바꾸어주기
                    # 카운트는 1 더해야하므로 저번방문위치에 1더해주기
                    q.append((x, y, w, -s, c + 1))
                    visited[x][y][w] = 1
                # 낮이다? -> 부실수있다
                else:
                    q.append((nx, ny, w + 1, -s, c + 1))
                    visited[nx][ny][w + 1] = 1
print(-1)
# print(visited)
