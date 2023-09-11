from itertools import combinations

l = int(input())

arr = list(map(int, input().split()))
arr.sort()
n = int(input())

if n in arr:
    print(0)
else:
    max = 0
    min = 0
    for i in range(0, l - 1):
        if arr[i] < n and arr[i + 1] > n:
            max = arr[i + 1] - 1
            min = arr[i] + 1
    if min == 0 and max == 0:
        max = arr[0]-1
        min = 1
    li = [int(i) for i in range(min,max+1)]
    new = list(combinations(li,2))
    count = 0
    for x,y in new:
        if x <= n and n <= y:
            count += 1
    print(count)