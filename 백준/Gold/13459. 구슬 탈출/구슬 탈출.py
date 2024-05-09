import sys

input = sys.stdin.readline

from collections import deque


def bfs(xr, yr, xb, yb, count):
    q = deque()
    q.append((xr, yr, xb, yb, count))
    flag = True
    while q:
        xr, yr, xb, yb, count = q.popleft()

        if count > 10:
            print(0)
            return

        for i in range(4):
            nxr = xr
            nyr = yr
            nxb = xb
            nyb = yb
            rcount = 0
            bcount = 0
            while True:
                nxr += dx[i]
                nyr += dy[i]

                if arr[nxr][nyr] != '#' and arr[nxr][nyr] != 'O':
                    rcount += 1
                elif arr[nxr][nyr] == 'O':
                    break
                else:
                    nxr -= dx[i]
                    nyr -= dy[i]
                    break
            while True:
                nxb += dx[i]
                nyb += dy[i]

                if arr[nxb][nyb] != '#' and arr[nxb][nyb] != 'O':
                    bcount += 1
                elif arr[nxb][nyb] == 'O':
                    break
                else:
                    nxb -= dx[i]
                    nyb -= dy[i]
                    break

            if arr[nxb][nyb] == 'O':
                continue

            if arr[nxr][nyr] == 'O' and count <= 10:
                
                # if flag and arr[nxr][nyr] == 'O' and count <= 10:
                print(1)
                return

            if nxb == nxr and nyb == nyr:
                if bcount > rcount:
                    nxb -= dx[i]
                    nyb -= dy[i]
                else:
                    nxr -= dx[i]
                    nyr -= dy[i]

            if (nxr, nyr, nxb, nyb) not in visited:
                q.append((nxr, nyr, nxb, nyb, count + 1))
                visited.add((nxr, nyr, nxb, nyb))
    print(0)
    return


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

visited = set()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            xr, yr = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            xb, yb = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'O':
            xe, ye = i, j

visited.add((xr, yr, xb, yb))
bfs(xr, yr, xb, yb, 1)
