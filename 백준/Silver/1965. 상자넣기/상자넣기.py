from bisect import bisect_left

n = int(input())
arr = list(map(int,input().split()))

d = []
d.append(arr[0])

for i in range(n):
    if arr[i] > d[-1]:
        d.append(arr[i])
    else:
        index = bisect_left(d,arr[i])

        d[index] = arr[i]
print(len(d))