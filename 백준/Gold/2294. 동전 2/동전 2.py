n,k = map(int,input().split())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

d = [10001] * (k+1)
d[0] = 0
for i in arr:
    for j in range(i, k + 1):
        d[j] = min(d[j], d[j-i] + 1)

if d[k] == 10001:
    print(-1)
else:
    print(d[k])