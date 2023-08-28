# wind[0] -> 왼쪽 wind[1] -> 아래 wind[2] -> 오른쪽 wind[3] -> 위
wind = [
    [(0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (1, 1, 0.01),
     (-1, 1, 0.01)],
    [(2, 0, 0.05), (1, -1, 0.1), (1, 1, 0.1), (0, 2, 0.02), (0, -2, 0.02), (0, 1, 0.07), (0, -1, 0.07), (-1, 1, 0.01),
     (-1, -1, 0.01)],
    [(0, 2, 0.05), (-1, 1, 0.1), (1, 1, 0.1), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.01),
     (1, -1, 0.01)],
    [(-2, 0, 0.05), (-1, -1, 0.1), (-1, 1, 0.1), (0, 2, 0.02), (0, -2, 0.02), (0, 1, 0.07), (0, -1, 0.07), (1, 1, 0.01),
     (1, -1, 0.01)]]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def sand(x, y, d):
    # 그 자리에 있던 모래양
    here = arr[x][y]
    # 바람이 불어서 날아가야하므로 arr[x][y]를 0으로 바꿔준다.
    arr[x][y] = 0
    zz = 0
    for i in range(9):
        nx = x + wind[d][i][0]
        ny = y + wind[d][i][1]
        if 0 <= nx < n and 0 <= ny < n:
            arr[nx][ny] = int(arr[nx][ny] + here * wind[d][i][2])
            zz += int(here * wind[d][i][2])
        else:
            zz += int(here * wind[d][i][2])

    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n:

        arr[nx][ny] += here - zz


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
total_sand = 0
for i in range(n):
    for j in range(n):
        total_sand += arr[i][j]
tornado = []
for i in range(1, n):
    tornado.append(i)
    tornado.append(i)
tornado.append(n - 1)

x, y = n // 2, n // 2

d = 0

for i in tornado:
    count = 0
    while count < i:
        
        x += dx[d]
        y += dy[d]
        count += 1
        # 다음구역에 모래가 있다면
        if arr[x][y] > 0:
            sand(x, y, d)
    d = (d + 1) % 4
# print(arr)
total = 0
for i in range(n):
    for j in range(n):
        total += arr[i][j]

print(total_sand-total)