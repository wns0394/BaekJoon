import sys
from pprint import pprint

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# n*n 판
# k개의 말
n, k = map(int, input().split())

# 0은 흰색
# 1은 빨간색
# 2는 파란색
arr = [list(map(int, input().split())) for _ in range(n)]

horse = []
horse_d = []

chess = [[[] for _ in range(n)] for _ in range(n)]

for i in range(k):
    x, y, d = map(int, input().split())
    horse.append((x - 1, y - 1))
    horse_d.append(d - 1)
    chess[x - 1][y - 1].append(i)

result = 0

# print(horse,'말 초기')
# print(horse_d,'말 방향 초기')
# pprint(arr)
# pprint(chess)

while result <= 1000:
    result += 1

    for i in range(k):
        x, y = horse[i]
        d = horse_d[i]

        nx = x + dx[d]
        ny = y + dy[d]
        # print(i,'iiiiiii')
        # print(x,y,nx,ny,'xynxny')
        # 격자 안에 존재
        # 흰색 칸이라면
        # if arr[nx][ny] == 0:
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            # i번 위에 있는 애들 모두 대리고 이동
            chess[nx][ny].extend(chess[x][y][chess[x][y].index(i):])
            # i번 위치 갱신
            for j in range(chess[x][y].index(i), len(chess[x][y])):
                horse[chess[x][y][j]] = (nx, ny)
            # 원래 위치에 i번 위에 있는 애들까지 삭제시켜주기
            length = len(chess[x][y]) - chess[x][y].index(i)
            # print(length,'length')
            for _ in range(length):
                chess[x][y] .pop()
            if len(chess[nx][ny]) >= 4:
                print(result)
                sys.exit()
        # 격자 안에 존재하고
        # 빨간색 칸이라면
        # 순서 뒤집기
        elif 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
            # i번 위에 있는 애들 모두 대리고 이동
            chess[nx][ny].extend(chess[x][y][chess[x][y].index(i):][::-1])
            # i번 위치 갱신
            for j in range(chess[x][y].index(i),len(chess[x][y])):
                horse[chess[x][y][j]] = (nx, ny)
            # 원래 위치에 i번 위에 있는 애들까지 삭제시켜주기
            length = len(chess[x][y]) - chess[x][y].index(i)
            # print(length,'length')
            for _ in range(length):
                chess[x][y].pop()
            # chess[nx][ny] = chess[nx][ny][::-1]
            if len(chess[nx][ny]) >= 4:
                print(result)
                sys.exit()
        # 격자안에 존재하지 않거나 파란색이라면
        else:
            if d in [0,2]:
                d += 1
            elif d in [1,3]:
                d -= 1

            horse_d[i] = d

            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                # i번 위에 있는 애들 모두 대리고 이동
                chess[nx][ny].extend(chess[x][y][chess[x][y].index(i):])
                # i번 위치 갱신
                for j in range(chess[x][y].index(i), len(chess[x][y])):
                    horse[chess[x][y][j]] = (nx, ny)
                # 원래 위치에 i번 위에 있는 애들까지 삭제시켜주기
                length = len(chess[x][y]) - chess[x][y].index(i)
                # print(length,'length')
                for _ in range(length):
                    chess[x][y].pop()
                if len(chess[nx][ny]) >= 4:

                    print(result)
                    sys.exit()
            # 격자 안에 존재하고
            # 빨간색 칸이라면
            # 순서 뒤집기
            elif 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                # i번 위에 있는 애들 모두 대리고 이동
                chess[nx][ny].extend(chess[x][y][chess[x][y].index(i):][::-1])
                # i번 위치 갱신
                for j in range(chess[x][y].index(i), len(chess[x][y])):
                    horse[chess[x][y][j]] = (nx, ny)
                # 원래 위치에 i번 위에 있는 애들까지 삭제시켜주기
                length = len(chess[x][y]) - chess[x][y].index(i)
                # print(length,'length')
                for _ in range(length):
                    chess[x][y].pop()
                # chess[nx][ny] = chess[nx][ny][::-1]
                if len(chess[nx][ny]) >= 4:
                    print(result)
                    sys.exit()

    # print(horse)
    # print(horse_d)
    # pprint(chess)
print(-1)