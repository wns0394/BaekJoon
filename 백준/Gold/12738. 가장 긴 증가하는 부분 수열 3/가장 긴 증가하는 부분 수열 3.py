from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

d = []
# dp 배열에 arr[0] 추가
d.append(arr[0])

for i in range(n):
    # 현재위치의 arr값이 이전 원소보다 크다면
    if arr[i] > d[-1]:
        # dp 배열에 추가
        d.append(arr[i])
    # 작거나 같다면
    else:
        # 이전 위치의 원소 중 가장 큰 원소의 index값을 구하고
        idx = bisect_left(d,arr[i])
        # 그 index의 원소를 arr[i]로 바꿔준다.
        d[idx] = arr[i]
    
print(len(d))