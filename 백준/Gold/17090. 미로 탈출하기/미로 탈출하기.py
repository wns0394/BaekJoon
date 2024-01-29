import sys

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    global count

    # x,y 방문처리
    visited[x][y] = 1
    q = deque()
    q.append((x, y))

    # 탈출 가능한지 여부 flag
    flag = False

    # 지금 bfs도는 동안 탐색한 경로를 담기위한 now
    now = []
    # 현재 지점 x,y도 now에 넣어주기
    now.append((x,y))

    while q:
        x, y = q.popleft()

        if arr[x][y] == 'D':
            nx = x + 1
            ny = y
        elif arr[x][y] == 'U':
            nx = x - 1
            ny = y
        elif arr[x][y] == 'L':
            nx = x
            ny = y - 1
        elif arr[x][y] == 'R':
            nx = x
            ny = y + 1

        # 다음에 이동할 장소가 격자안에 존재하고 방문한적이 없다면
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            # 방문처리해주고 현재 탐색할 경로 now에 추가해주기
            q.append((nx, ny))
            visited[nx][ny] = 1
            now.append((nx, ny))

        # 만약 격자 밖
        # 즉 탈출 가능하다면
        elif nx < 0 or nx >= n or ny < 0 or ny >= m:
            # count + 1 해주고
            # 탈출 가능하므로 flag 는 True로 바꿔주고 break 중단
            count += 1
            flag = True
            break

        # 다음지점 nx,ny가 check안에 존재한다면
        # 이 지점 또한 탙출 가능한 지점이므로 count + 1 해주고 flag는 True로 바꿔주고 break
        elif (nx, ny) in check:
            count += 1
            flag = True
            break

    # 만약 탈출이 불가능하다면
    # 무한 루프인것이므로
    if not flag:
        # 현재 탐색한 경로의 모든 (a,b)좌표를
        # 루프에 담아주기
        for a, b in now:
            roop.add((a,b))

    # 탈출 가능하다면
    else:
        # 현재 탐색한 경로의 모든 (a,b)좌표를
        # 탈출 가능한 경로 check에 담아주기
        for a,b in now:
            check.add((a,b))


n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

count = 0

# 그 칸을 지났을 때 밖으로 탈출가능한 check
check = set()

# 그 칸을 지났을 때 안에서 무한 루프를 돌아 탈출 불가능한 roop
roop = set()


for i in range(n):
    for j in range(m):
        # 만약 i,j가 무한루프에 있으면 넘긴다.
        if (i,j) in roop:
            continue

        # 만약 i,j가 탈출가능한 도로에 있다면 count + 1
        if (i,j) in check:
            count += 1

        # bfs 실행
        else:
            bfs(i, j)

print(count)

