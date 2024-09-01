import sys

input = sys.stdin.readline

from collections import deque

arr = list(map(int, input().split()))

# f,s,g,u,d
# f층 존재 s층 시작 g층 도착 위로 u층 아래로 d층

q = deque()
q.append(arr[1])
visited = [0] * (arr[0] + 1)

visited[arr[1]] = 1
flag = False
while q:
    x = q.popleft()

    if x == arr[2]:
        print(visited[x] - 1)
        flag = True
        break
    for nx in (x+arr[3],x-arr[4]):
        if 1 <= nx < arr[0] + 1 and visited[nx] == 0:
            q.append(nx)
            visited[nx] = visited[x] + 1

if not flag:
    print('use the stairs')