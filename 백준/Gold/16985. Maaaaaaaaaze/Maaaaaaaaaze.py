from collections import deque
from itertools import permutations
from copy import deepcopy

# x,y,z 축 이동
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


# 90도 회전함수
def rotate(origin):
    rotate_arr = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            rotate_arr[i][j] = origin[j][5 - 1 - i]

    return rotate_arr


def dfs(cnt):
    # 5개의 판이 회전했으면
    if cnt == 5:
        # 출발지점과 도착지점이 1이여야지만 가능하므로
        # 그런 경우에만 bfs돌림
        if new[0][0][0] == 1 and new[4][4][4] == 1:
            bfs(new)
        return

    # 90도 회전 4번
    for i in range(4):
        # dfs실행
        dfs(cnt + 1)
        # 판 돌리기
        new[cnt] = rotate(new[cnt])


arr = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

# 최단거리 찾기 위한 bfs
def bfs(arr):
    global result
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    q = deque()

    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()

        # 도착지점에 도착하였으면
        if x == 4 and y == 4 and z == 4:
            # 최소값 반환
            result = min(result, visited[x][y][z] - 1)
            return

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                if arr[nx][ny][nz] == 1 and visited[nx][ny][nz] == 0:
                    q.append((nx, ny, nz))
                    visited[nx][ny][nz] = visited[x][y][z] + 1


result = 126
# 5*4*3*2*1 가지의 경우의 수
for i in list(permutations([0, 1, 2, 3, 4], 5)):
    new = [deepcopy(arr[i[0]]), deepcopy(arr[i[1]]), deepcopy(arr[i[2]]), deepcopy(arr[i[3]]), deepcopy(arr[i[4]])]

    dfs(0)

if result == 126:
    print(-1)
else:
    print(result)
