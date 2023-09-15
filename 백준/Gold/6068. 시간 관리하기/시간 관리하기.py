n = int(input())

arr = []

for _ in range(n):
    t,s = map(int,input().split())

    arr.append((t,s))

arr.sort(key= lambda x: (x[1],-x[0]))
result = 1000001
pre = 0
for i in range(n):
    if arr[i][1] - (pre+arr[i][0]) >= 0:
        pre += arr[i][0]
        result = min(result,arr[i][1] -pre)
    else:
        result = -1
        break
print(result)