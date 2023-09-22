import heapq

n = int(input())

arr = []

for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])

arr.sort()

result = []
for i in range(n):
    heapq.heappush(result,arr[i][1])

    if arr[i][0] < len(result):
        heapq.heappop(result)
print(sum(result))