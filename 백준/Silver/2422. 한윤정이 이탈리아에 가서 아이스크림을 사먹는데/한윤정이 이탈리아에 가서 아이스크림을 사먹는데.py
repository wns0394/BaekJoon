from itertools import combinations

# n : 아이스크림 종류의 수 1 <= n <= 200
# m : 섞어먹으면 안되는 조합의 개수 0 <= m <= 10000
n, m = map(int, input().split())

ice = list(combinations(range(1, n+1), 3))
arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1
count = 0
for i in ice:
    if arr[i[0]][i[1]] or arr[i[0]][i[2]] or arr[i[1]][i[2]]:
        continue
    count += 1
print(count)