from copy import deepcopy

n = int(input())

arr = []

for _ in range(n):
    num = list(map(int,input().split()))
    arr.append(num)

d = deepcopy(arr)

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            d[i][j] += d[i-1][j]
        elif j == i:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] += max(d[i-1][j-1],d[i-1][j])
print(max(d[-1]))