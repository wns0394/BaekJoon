
import heapq
# 0 < n <= 1500
# 2중 for문 빡신데 아닌가
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in arr[0]:
    heapq.heappush(result, i)

for i in range(1,n):
    for j in arr[i]:
        if result[0] < j:
            heapq.heappush(result, j)
            heapq.heappop(result)
print(result[0])