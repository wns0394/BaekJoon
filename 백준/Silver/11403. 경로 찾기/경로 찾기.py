n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for a in range(n):
        for b in range(n):
            if arr[a][i] == 1 and arr[i][b] == 1:
                arr[a][b] = 1

for i in arr:
    print(*i)