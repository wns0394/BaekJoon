from collections import deque

n, t = map(int, input().split())

arr = set()

for _ in range(n):
    x, y = map(int, input().split())

    arr.add((x, y))

q = deque()
q.append((0, 0, 0))
flag = False
while q:
    x, y, count = q.popleft()
    if y == t:
        flag = True
        break
    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = x + i
            ny = y + j

            if (nx, ny) in arr:
                q.append((nx, ny, count + 1))
                arr.remove((nx, ny))

if flag:
    print(count)
else:
    print(-1)