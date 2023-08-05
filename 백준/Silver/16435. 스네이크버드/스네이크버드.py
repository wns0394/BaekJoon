import sys
n,l = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

result = l
for i in range(n):
    if arr[i] <= result:
        result += 1
    else:
        break
print(result)