n,m = map(int,input().split())

inf = int(1e9)

arr = [[inf] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a][b] = c

for i in range(1,n+1):
    arr[i][i] = 0

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            arr[a][b] = min(arr[a][b], arr[a][i] + arr[i][b])

# print(arr)

k = int(input())
city = list(map(int,input().split()))

result = []
for x in range(1,n+1):
    max_result = 0
    for i in city:
        if i != x and arr[i][x] != inf and arr[x][i] != inf:
            max_result = max(max_result, arr[i][x] + arr[x][i])
    result.append(max_result)

# print(result)
min_result = min(result)

for i in range(n):
    if result[i] == min_result:
        print(i+1, end=' ')