
n,m = map(int,input().split())

arr = list(map(int,input().split()))

start = 0
end = min(arr) * m

while start+1 < end:
    mid = (start+end) // 2
    result = 0

    for i in range(n):
        result += mid//arr[i]

    if result >= m:
        end = mid
    else:
        start = mid

print(end)
