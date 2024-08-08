import sys

input = sys.stdin.readline

t = int(input())


def rotate_45():
    new = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                new[i][n // 2] = arr[i][j]
            elif j == n // 2:
                new[i][n - 1 - i] = arr[i][j]
            elif i == n // 2:
                new[j][j] = arr[i][j]
            elif i + j == n - 1:
                new[n // 2][j] = arr[i][j]
            else:
                new[i][j] = arr[i][j]

    return new


for _ in range(t):
    # n은 홀수
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    new = [[0] * n for _ in range(n)]

    if 0 < d // 45 < 8:
        for i in range(1, (d // 45) + 1):
            arr = rotate_45()
    elif -8 < d // 45 < 0:
        for i in range(1, 8 + (d // 45) + 1):
            arr = rotate_45()

    for i in range(n):
        print(*arr[i])
