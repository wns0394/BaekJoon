dx = [1,0]
dy = [0,1]

def dfs(x,y):
    global li, maxresult,minresult
    visited[x][y] = 1

    if x == n-1 and y == n-1:
        total = 0
        for i in range(len(li)):
            if i == 0:
                if li[i].isnumeric():
                    total = int(li[i])
            if i > 0:
                if li[i-1] == '*':
                    total = total * int(li[i])
                elif li[i-1] == '+':
                    total = total + int(li[i])
                elif li[i-1] == '-':
                    total = total - int(li[i])
        if total > maxresult:
            maxresult = total
        if total < minresult:
            minresult = total
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            visited[nx][ny] = 1
            li.append(arr[nx][ny])
            dfs(nx,ny)
            visited[nx][ny] = 0
            li.pop()

n = int(input())

arr = [list(map(str,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
li = []
li.append(arr[0][0])
maxresult = -100000
minresult = 1000000
dfs(0,0)

print(maxresult,minresult)