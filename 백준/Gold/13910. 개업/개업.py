n,m = map(int,input().split())

# 같은 크기의 웍을 여러개 가지고 있을 수 있다.
arr = list(map(int,input().split()))

# 한손으로 가능한거랑 두손으로 가능한 요리 수를 추가해주자
for i in range(m):
    for j in range(i,m):
        # 자기자신을 더하는거는 넘기고
        if i == j:
            continue
        # 서로 다른 아이들에서
        # 만들어야하는 짜장면 개수보다 작거나 같고 원래 안에 없으면 추가
        if arr[i] + arr[j] <= n and arr[i] + arr[j] not in arr:
            arr.append(arr[i] + arr[j])

# 웍 1개 혹은 2개를 이용해서 만들 수 있는 경우의 수 모두 나옴
a = set(arr)

d = [100001] * (n+1)
d[0] = 0
# 만들 수 있는 개수
for i in a:
    for j in range(i, n + 1):
        # 현재 개수와 j-i 개수 에서 1개 더한값 비교
        d[j] = min(d[j], d[j - i] + 1)
if d[n] != 100001:
    print(d[n])
else:
    print(-1)