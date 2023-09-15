def dfs(start,cost,count):
    global result
    if count == n-1 and arr[start][0] != 0:
        result = min(result,cost+arr[start][0])
        return

    for i in range(n):
        if visited[i] == 0 and arr[start][i] != 0:
            visited[i] = 1
            dfs(i,cost+arr[start][i],count+1)
            visited[i] = 0

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n

result = int(1e9)

visited[0] = 1
dfs(0,0,0)
print(result)