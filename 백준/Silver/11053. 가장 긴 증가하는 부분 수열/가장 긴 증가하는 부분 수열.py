n = int(input())
arr = list(map(int,input().split()))
# d에는 i번째 가장 긴 부분수열의 길이를 넣을것이다.
d = [0 for _ in range(1001)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
print(max(d))