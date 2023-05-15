
import heapq

n = int(input())

arr = []
for i in range(n):
    s,t = map(int,input().split())
    arr.append((s,t))

arr.sort(key=lambda x : (x[0], x[1]))
h = []
heapq.heappush(h,arr[0][1])
for i in range(1,n):
    # 시작시간이 끝나는 시간보다 빠르다면
    if arr[i][0] < h[0]:
        # 힙에 끝나는 시간 저장
        heapq.heappush(h,arr[i][1])
    # 시작시간이 끝나는 시간보다 뒤라면
    else:
        #  힙 삭제
        heapq.heappop(h)
        # 끝나는 시간 저장
        heapq.heappush(h, arr[i][1])

print(len(h))