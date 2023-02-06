
from collections import deque


def bfs():
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        x = q.popleft()

        if x == k:
            return visited[x]-1

        for next in (x-1, x+1, x*2):
            if 0 <= next <100001 and visited[next] == 0:
                q.append(next)
                visited[next] = visited[x] + 1
n, k = map(int,input().split())

visited= [0] * (100001)

print(bfs())