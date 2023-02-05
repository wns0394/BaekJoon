from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    q = deque()
    # 0,0에 0번 뚫었다
    q.append((0,0,0))
    # 방문처리
    visited[0][0][0] = 1

    while q:
        # x,y 좌표랑 w : 얼마나 부셨는지
        x, y, w = q.popleft()

        # 종료조건 n,m에 위치했을때
        if x == n-1 and y == m-1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 배열안에 있고
            if 0 <= nx < n and 0 <= ny < m:
                # 이동가능하고 방문한적이 없으면
                if arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    # 다음 좌표랑 벽 부신 수  w 그대로 저장
                    q.append((nx, ny, w))
                    #  저번 방문처리 + 1
                    visited[nx][ny][w] = visited[x][y][w] + 1
                # 벽이고 벽 부신 횟수가 k 보다 작다면 그리고 방문한적이 없으면
                elif arr[nx][ny] == 1 and w < k and visited[nx][ny][w+1] == 0:
                    # 다음 좌표와 벽 부신 횟수 1 추가
                    q.append((nx, ny, w+1))
                    # 방문한거좌표에다가 부신횟수 1 추가한곳이
                    # 저번 방문한좌표와 저번 부신 곳 + 1
                    visited[nx][ny][w+1] = visited[x][y][w] + 1
    return -1
n, m, k = map(int,input().split())

arr = [list(map(int,input())) for _ in range(n)]

# k+1 해주는 이유는 벽을 0번부터 k번 까지 뚫을 수 있으므로
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]

print(bfs())