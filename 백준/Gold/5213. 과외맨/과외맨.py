from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    path[x][y] = 0

    while q:
        x, y = q.popleft()

        # 1,3,5번째 줄 index 때문에 짝수로 조건을 줌
        if x % 2 == 0:
            if 0 <= y < n:
                # 아래 왼쪽 아래 왼쪽은 y index가 하나 작다
                # 아래쪽이므로 y 인덱스는 n-2까지밖에 없다
                if 0 <= x + 1 < n and 0 <= y - 1 < n - 1 and arr[x][y][0] == arr[x + 1][y - 1][1] and path[x + 1][
                    y - 1] == 0:
                    q.append((x + 1, y - 1))
                    path[x + 1][y - 1] = (x, y)

                # 아래 오른쪽 (x+1,y) 아래 오른쪽은 y index가 같다
                # 아래쪽이므로 y 인덱스는 n-2까지밖에 없다
                if 0 <= x + 1 < n and 0 <= y < n - 1 and arr[x][y][1] == arr[x + 1][y][0] and path[x + 1][y] == 0:
                    q.append((x + 1, y))
                    path[x + 1][y] = (x, y)

                # 위 왼쪽 y인덱스가 하나 작다
                # 위쪽이므로 y 인덱스는 n-2까지밖에 없다
                if 0 <= x - 1 < n and 0 <= y - 1 < n - 1 and arr[x][y][0] == arr[x - 1][y - 1][1] and path[x - 1][
                    y - 1] == 0:
                    q.append((x - 1, y - 1))
                    path[x - 1][y - 1] = (x, y)

                # 위 오른쪽 y인덱스가 같다
                # 위쪽이므로 y 인덱스는 n-2까지밖에 없다
                if 0 <= x - 1 < n and 0 <= y < n - 1 and arr[x][y][1] == arr[x - 1][y][0] and path[x - 1][y] == 0:
                    q.append((x - 1, y))
                    path[x - 1][y] = (x, y)

                # 오른쪽
                if 0 <= x < n and 0 <= y + 1 < n and arr[x][y][1] == arr[x][y + 1][0] and path[x][y + 1] == 0:
                    q.append((x, y + 1))
                    path[x][y + 1] = (x, y)

                # 왼쪽
                if 0 <= x < n and 0 <= y - 1 < n and arr[x][y][0] == arr[x][y - 1][1] and path[x][y - 1] == 0:
                    q.append((x, y - 1))
                    path[x][y - 1] = (x, y)

        # 2,4,6번째 줄 index 때문에 홀수로 조건을 줌
        # n-1개의 타일만 존재
        else:
            if 0 <= y < n - 1:

                # 아래 왼쪽
                if 0 <= x + 1 < n and 0 <= y < n and arr[x][y][0] == arr[x + 1][y][1] and path[x + 1][y] == 0:
                    q.append((x + 1, y))
                    path[x + 1][y] = (x, y)

                # 아래 오른쪽
                if 0 <= x + 1 < n and 0 <= y + 1 < n and arr[x][y][1] == arr[x + 1][y + 1][0] and path[x + 1][
                    y + 1] == 0:
                    q.append((x + 1, y + 1))
                    path[x + 1][y + 1] = (x, y)

                # 위 왼쪽
                if 0 <= x - 1 < n and 0 <= y < n and arr[x][y][0] == arr[x - 1][y][1] and path[x - 1][y] == 0:
                    q.append((x - 1, y))
                    path[x - 1][y] = (x, y)

                # 위 오른쪽
                if 0 <= x - 1 < n and 0 <= y + 1 < n and arr[x][y][1] == arr[x - 1][y + 1][0] and path[x - 1][
                    y + 1] == 0:
                    q.append((x - 1, y + 1))
                    path[x - 1][y + 1] = (x, y)

                # 오른쪽
                if 0 <= x < n and 0 <= y + 1 < n - 1 and arr[x][y][1] == arr[x][y + 1][0] and path[x][y + 1] == 0:
                    q.append((x, y + 1))
                    path[x][y + 1] = (x, y)

                # 왼쪽
                if 0 <= x < n and 0 <= y - 1 < n - 1 and arr[x][y][0] == arr[x][y - 1][1] and path[x][y - 1] == 0:
                    q.append((x, y - 1))
                    path[x][y - 1] = (x, y)
    return path


n = int(input())

arr = []
path = [[0] * (n - 1) for _ in range(n)]
check = [[0] * (n - 1) for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        arr.append(list([0, 0] for _ in range(n)))
        path[i].append(0)
        check[i].append(0)
    else:
        arr.append(list([0, 0] for _ in range(n - 1)))

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            x, y = map(int, input().split())
            arr[i][j] = [x, y]
    else:
        for j in range(n - 1):
            x, y = map(int, input().split())
            arr[i][j] = [x, y]

a = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            check[i][j] = a
            a += 1
    else:
        for j in range(n - 1):
            check[i][j] = a
            a += 1

bfs(0, 0)
for i in range(n):
    if i % 2 == 1:
        path[i].append(0)

result = []

flag = 0
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if path[i][j] != 0:
            result.append(check[i][j])
            x, y = i, j
            while True:
                if path[x][y] != 0:
                    nx = path[x][y][0]
                    ny = path[x][y][1]
                    x, y = nx, ny
                    result.append(check[x][y])
                if x == 0 and y == 0:
                    flag = 1
                    break
            if flag:
                break
    if flag:
        break

result.reverse()
if len(result) == 0:
    print(1)
    print(1)
else:
    print(len(result))
    print(*result)
