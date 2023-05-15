n = int(input())

arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.append((arr[0][0], arr[0][1]))

a = 0
b = 0
for i in range(n):
    a += arr[i][0] * arr[i+1][1]
    b += arr[i][1] * arr[i+1][0]

print(round(abs(a-b)/2,1))