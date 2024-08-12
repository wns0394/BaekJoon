import sys

from collections import deque

from itertools import permutations

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == '.' and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif arr[nx][ny] == '*' and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif arr[nx][ny] == 'o':
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited


while True:
    m, n = map(int, input().split())

    if n == 0 and m == 0:
        sys.exit()
    arr = [list(input().rstrip()) for _ in range(n)]

    sx = 0
    sy = 0

    dirty = []

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'o':
                sx = i
                sy = j
            if arr[i][j] == '*':
                dirty.append((i, j))

    # 시작위치로부터 모든칸의 이동 거리를 측정한 di
    di = bfs(sx, sy)

    # 로봇청소기가 모든 먼지에 갈 수 있는지 체크하기 위한 flag
    flag = True

    # 시작점 부터 먼지까지의 거리를 알기 위한 sto
    sto = []

    # 모든 먼지의 좌표에
    for x, y in dirty:
        # 로봇청소기가 도달할 수 없다면
        if di[x][y] == 0:
            # flag 는 False
            flag = False
            print(-1)
            break
        # 도달한다면
        else:
            # 시작지점부터 먼지까지의 거리 리스트에 넣어주기
            sto.append((di[x][y] -1))
    
    # 불가능하다면 다음 작업은 무의미
    if flag == False:
        continue

    k = len(dirty)

    # 각 먼지들 사이의 거리를 저장하기 위한 distance
    distance = [[0]*k for _ in range(k)]

    # 각먼지들의 거리 구하기
    # i가 출발지 j가 도착지
    for i in range(k-1):
        # 출발지에 대한 bfs 정보
        c = bfs(dirty[i][0], dirty[i][1])
        for j in range(i+1,k):
            # 도착지 까지의 거리를 담아주기
            distance[i][j] = c[dirty[j][0]][dirty[j][1]] - 1
            # 출발 도착지가 바뀌어도 거리는 같다
            distance[j][i] = distance[i][j]

    result = int(1e9)

    # 인덱스로 편하게 하기 위해
    v = [int(i) for i in range(k)]
    # 인덱스로 permutations 작성
    p = list(permutations(v,k))

    len_p = len(p)

    for i in range(len_p):
        # 각각의 경우마다 거리를 확인하기 위한 count
        count = 0
        # 우선적으로 시작지점과 첫번째로 정하는 먼지의 거리를 더해준다.
        count += sto[p[i][0]]

        # 다음 순열부터 앞 뒤 거리를 구해서 count에 더해준다
        for j in range(len(p[i])-1):
            count += distance[p[i][j]][p[i][j+1]]
        # 최소값으로 갱신
        if count < result:
            result = count
    print(result)
