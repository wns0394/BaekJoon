from itertools import combinations
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = [int(i) for i in range(1,n)]
    li = list(combinations(arr,2))

    count = 0
    for i in range(len(li)):
        a = li[i][0]
        b = li[i][1]

        if (a**2 + b**2 + m) % (a*b) == 0:
            count += 1
    print(count)
