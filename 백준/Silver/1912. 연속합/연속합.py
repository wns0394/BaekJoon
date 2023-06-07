n = int(input())
arr = list(map(int,input().split()))
# 최대합을 저장할 d 생성
d = [0] * n

d[0] = arr[0]
# 1부터 n까지
for i in range(1,n):
    # i번째의 최대는 i-1번째의 최대합에서 i번째를 더했을때 누가 더 최대인지 정하면 된다.
    d[i] = max(arr[i], d[i-1] + arr[i])
print(max(d))