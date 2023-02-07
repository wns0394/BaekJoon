
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        x = q.popleft()

        if x == g:
            return visited[x] - 1
        for next in (x+u, x-d):
            if 0 < next < (f+1) and visited[next] == 0:
                q.append(next)
                visited[next] = visited[x] + 1
    return "use the stairs"

f, s, g, u, d = map(int,input().split())
visited = [0] * (f+1)

print(bfs(s))