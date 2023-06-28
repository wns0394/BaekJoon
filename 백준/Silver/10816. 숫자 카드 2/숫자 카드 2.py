from collections import Counter

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

c = Counter(arr1)

for i in arr2:
    if i in c:
        print(c[i], end=' ')
    else:
        print(0, end=' ')