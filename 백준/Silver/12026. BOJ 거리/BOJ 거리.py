n = int(input())
arr = list(input())

d = [1000000] * n
d[0] = 0
for i in range(n):
    for j in range(i):
        if arr[i] == 'B' and arr[j] == 'J':
            d[i] = min(d[i],d[j] + (i-j)*(i-j))
        if arr[i] == 'O' and arr[j] == 'B':
            d[i] = min(d[i],d[j] + (i-j)*(i-j))
        if arr[i] == 'J' and arr[j] == 'O':
            d[i] = min(d[i],d[j] + (i-j)*(i-j))

if d[-1] == 1000000:
    print(-1)
else:
    print(d[-1])