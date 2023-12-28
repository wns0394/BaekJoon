def dfs(L):
    visited[L] = 1

    print(L, end=' ')
    for i in data[L]:
        if visited[i] == 1:
            continue
        dfs(i)

def bfs(s):
    q = []
    vi = [0] * (n + 1)
    q.append(s)
    vi[s] = 1

    while q:
        a = q.pop(0)
        print(a, end=' ')

        for i in data[a]:
            if vi[i] == 0:
                q.append(i)
                vi[i] = 1
#  정점 개수 n, 간선의 개수 m, 정점의 번호 v
n, m, v = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(m)]


# print(arr)

# 인접행렬
data = [[] for _ in range(n+1)]

for i in range(m):
    data[arr[i][0]].append(arr[i][1])
    data[arr[i][1]].append(arr[i][0])

# print(data,"정렬전")
for i in data:
    i.sort()
#
# print(data)

# 방문행렬
visited = [0] * (n+1)

dfs(v)
print()
bfs(v)