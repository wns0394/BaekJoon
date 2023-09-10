from itertools import combinations

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

li = [int(i) for i in range(n)]

all = list(combinations(li, n // 2))

result = int(1e9)
for i in range(len(all) // 2):
    start = 0
    link = 0
    startteam = list(all[i])
    linkteam = set(li) - set(startteam)
    for x, y in list(combinations(startteam, 2)):
        start += arr[x][y]
        start += arr[y][x]
    for x, y in list(combinations(linkteam, 2)):
        link += arr[x][y]
        link += arr[y][x]
    result = min(result,abs(start-link))
print(result)