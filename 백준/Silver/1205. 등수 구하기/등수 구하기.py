n, score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    arr = list(map(int,input().split()))
    if n == p and arr[-1] >= score:
        print(-1)
    else:
        count = n+1
        for i in range(n):
            if arr[i] <= score:
                count = i+1
                break
        print(count)