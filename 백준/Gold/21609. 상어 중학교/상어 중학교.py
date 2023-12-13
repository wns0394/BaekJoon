
from collections import deque
from copy import deepcopy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rotate():
    global arr
    new = [[0] * n for _ in range(n)]

    # 90도 반시계방향 회전
    # 1행 -> 1열, 2행 -> 2열,,,,
    # 00 04, 01 14, 02 24, 03 34, 04 44
    # 10 03, 11 13, 12 23, 13 33,

    for i in range(n):
        for j in range(n):
            new[i][j] = arr[j][n - 1 - i]

    arr = deepcopy(new)
    return arr


def drop():
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, -1, -1):
            cnt = 0
            if arr[i][j] >= 0:
                while True:
                    cnt += 1
                    if i + cnt >= n:
                        break
                    if arr[i + cnt][j] >= -1:
                        break

                if cnt > 1:
                    arr[i + cnt - 1][j] = arr[i][j]
                    arr[i][j] = -2
    return arr


def find():
    global score

    visited = [[0] * n for _ in range(n)]

    color = 0
    rainbow = 0
    big = []
    standard_x = 0
    standard_y = 0
    for i in range(n):
        for j in range(n):
            # print(i,j,arr[i][j],visited[i][j])
            if arr[i][j] > 0 and visited[i][j] == 0:
                # print((i,j))
                q = deque()
                q.append((i, j))
                visited[i][j] = 1
                now_color = 0
                now_rainbow = 0
                now_color += 1
                now = arr[i][j]
                # print(now)
                group = []
                group.append((i, j))
                standard = []
                standard.append((i, j))
                while q:
                    x, y = q.popleft()

                    for a in range(4):
                        nx = x + dx[a]
                        ny = y + dy[a]

                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] == now and visited[nx][ny] == 0:
                                # print(nx,ny,'nxny')
                                q.append((nx, ny))
                                visited[nx][ny] = 1
                                now_color += 1
                                group.append((nx, ny))
                                standard.append((nx, ny))

                            elif arr[nx][ny] == 0 and (nx, ny) not in group:
                                q.append((nx, ny))
                                now_rainbow += 1
                                group.append((nx, ny))

                standard.sort()

                now_standard_x = standard[0][0]
                now_standard_y = standard[0][1]

                # print(now_color,now_rainbow)
                # print(group)
                # print('---------------------')
                # if now_color + now_rainbow < 2:
                #     break

                if now_color + now_rainbow > color + rainbow:
                    color = now_color
                    rainbow = now_rainbow
                    big = group
                    standard_x = now_standard_x
                    standard_y = now_standard_y
                if now_color + now_rainbow == color + rainbow:
                    if now_rainbow > rainbow:
                        color = now_color
                        rainbow = now_rainbow
                        big = group
                        standard_x = now_standard_x
                        standard_y = now_standard_y
                    elif color > now_color:
                        color = color
                        rainbow = rainbow
                        big = big
                        standard_x = standard_x
                        standard_y = standard_y
                    elif now_color == color:
                        if now_standard_x > standard_x:
                            big = group
                            standard_x = now_standard_x
                            standard_y = now_standard_y

                        if now_standard_x == standard_x and now_standard_y > standard_y:
                            big = group
                            standard_x = now_standard_x
                            standard_y = now_standard_y

    if color + rainbow >= 2:
        score += (color + rainbow) ** 2
        for x, y in big:
            arr[x][y] = -2
        flag = 0
    else:
        flag = 1
    # print(score)
    return flag
    # print(color,rainbow,big)


# n*n 격자 m개 색상의 일반 블록
n, m = map(int, input().split())

# 검은색 블록 -1
# 무지개 블록 0
# 일반 블록 m 이하의 자연수
arr = [list(map(int, input().split())) for _ in range(n)]

# 연결된 블록의 집합 조건
# 일반 블록이 적어도 하나 존재 일반 블록의 색은 모두 같아야 함
# 검은색 블록은 포함 x 무지개 블록은 상관없음
# 그룹의 블록의 개수는 2이상
# 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동가능해야한다.

# 크기가 가장 큰 블록 그룹을 찾는다.
# 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹,
# 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을,
# 그 것도 여러개이면 열이 가장 큰 것을 찾는다.

score = 0
while True:
    # find()
    if find() == 1:
        break
    # for a in range(n):
    #     print(*arr[a])
    # print('-------부심--------')
    drop()
    # for a in range(n):
    #     print(*arr[a])
    # print('-------1차 떨굼--------')
    rotate()
    # for a in range(n):
    #     print(*arr[a])
    # print('-------회전--------')
    drop()
    # for a in range(n):
    #     print(*arr[a])
    # print('-------2차 떨굼--------')
print(score)
