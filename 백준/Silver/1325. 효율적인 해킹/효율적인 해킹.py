from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited = [0] * (n+1)
    visited[x] = 1
    count = 1

    while q:
        x = q.popleft()

        for i in arr[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                count += 1
    return count

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

result = []
for i in range(1,n+1):
    result.append(bfs(i))

maxnum = max(result)
for i in range(len(result)):
    if result[i] == maxnum:
        print(i+1, end = ' ')