import sys

from pprint import pprint
from collections import deque
from itertools import combinations

input = sys.stdin.readline


# S : 이다솜파
# Y : 임도연파

def check_7(a):
    q = deque()
    q.append((a[0][0], a[0][1]))

    visited = [0] * 7

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx, ny) in a and visited[a.index((nx, ny))] == 0:
                q.append((nx, ny))
                visited[a.index((nx, ny))] = 1
    if 0 in visited:
        return False
    return True


def check_4(a):
    count = 0

    for x, y in a:
        if arr[x][y] == 'S':
            count += 1

    if count >= 4:
        return True
    return False


n = 5

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = [list(input().rstrip()) for _ in range(5)]

result = 0

index = []
for i in range(5):
    for j in range(5):
        index.append((i, j))
comb = list(combinations(index, 7))

result = 0
for i in comb:
    if check_7(i):
        if check_4(i):
            result += 1

print(result)
