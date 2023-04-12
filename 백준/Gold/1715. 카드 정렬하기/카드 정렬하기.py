import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap,int(input()))

result = 0
while True:
    if len(heap) == 1:
        print(result)
        break
    else:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        result += x+y

        heapq.heappush(heap,x+y)