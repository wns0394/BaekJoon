
from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001
# print(visited)

q = deque()
q.append(n)
visited[n] = 0

while q:
    x = q.popleft()
    if k <= n:
        print(n-k)
        break
    if x == k:
        print(visited[k])
        break
    for next in (x - 1, x + 1, x * 2):
        if 0 <= next < 100001 and visited[next] == 0:
            if next == x * 2 and next !=0:
                q.appendleft(next)
                visited[next] = visited[x]
            else:
                q.append(next)
                visited[next] = visited[x] + 1
