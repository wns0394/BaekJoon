
from collections import deque
from itertools import combinations

# 4방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 상대바둑돌이고 방문한적 없다면
                if arr[nx][ny] == 2 and visited[nx][ny] == 0:
                    # 방문표시 및 큐에 담기
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                # 주변에 비어있는 공간이 있다면
                # group리스트에 담아주기
                # group -> 0이 들어갈 수 있는 자리
                if arr[nx][ny] == 0:
                    group.append((nx, ny))


def newbfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    # 상대돌 개수 세기 위한 twocount
    twocount = 0
    # 주변에 0이 존재하는지 체크하기 위한 flag
    flag = 0
    while q:
        x, y = q.popleft()
        # 상대돌 한개 증가
        twocount += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 상대돌이고 방문한적없으면 방문처리하고 큐에 담기
                if arr[nx][ny] == 2 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                # 주변에 0이 존재하면 flag = 1
                if arr[nx][ny] == 0:
                    flag = 1

    return twocount, flag


n, m = map(int, input().split())

# 0: 빈칸, 1: 내 돌, 2: 상대 돌
arr = [list(map(int, input().split())) for _ in range(n)]

# 결과값을 위한 result
result = 0

visited = [[0] * m for _ in range(n)]

# 0이 들어갈 수 있는 좌표들을 저장하기위한 리스트
possible = []

for i in range(n):
    for j in range(m):
        # 그룹별로 주변에 0이 몇개인지 세어주기 위해서
        # 만약 한 그룹에서 주변에 0이 3개 이상이라면 바둑돌 2개를 두어도 못잡으니까
        # possible리스트에 담지 않는다
        group = []
        # 상대 바둑돌 탐색
        if arr[i][j] == 2 and visited[i][j] == 0:
            bfs(i, j)
            # 그룹의 길이가 2이하인 애들만 possible리스트에 담아준다
            if len(set(group)) <= 2:
                possible += group
# 중복제거
possible = list(set(possible))

# 만약 바둑을 둘곳이 하나라면
if len(possible) == 1:
    # 그 좌표만 1로 바꾸어주고
    arr[possible[0][0]][possible[0][1]] = 1

    # 죽일 수 있는 돌의 합
    alltwo = 0

    visited = [[0] * m for _ in range(n)]
    for a in range(n):
        for b in range(m):
            # 상대돌 탐색
            if arr[a][b] == 2 and visited[a][b] == 0:
                # twocount : 2의 개수
                # flag : 주변에 0 이 존재하는지
                twocount, flag = newbfs(a, b)
                # 주변에 0이 존재하지 않는다면
                # 즉 상대돌을 죽일 수 있다면
                if flag != 1:
                    # 더해주자
                    alltwo += twocount
    # 더 큰값으로 갱신
    result = max(result, alltwo)
# 바둑을 둘 수 있는 곳이 여러곳이라면
else:
    # 모든 조합을 allpossible 리스트에 저장
    allpossible = list(combinations(possible, 2))

    for i in allpossible:

        # 가능한 위치를 내 돌로 변환
        arr[i[0][0]][i[0][1]] = 1
        arr[i[1][0]][i[1][1]] = 1

        alltwo = 0
        visited = [[0] * m for _ in range(n)]
        for a in range(n):
            for b in range(m):
                if arr[a][b] == 2 and visited[a][b] == 0:
                    twocount, flag = newbfs(a, b)
                    if flag != 1:
                        alltwo += twocount
        result = max(result, alltwo)

        # 내돌둔거 다시 초기화
        # 다른돌을 두어야하므로
        arr[i[0][0]][i[0][1]] = 0
        arr[i[1][0]][i[1][1]] = 0
print(result)
