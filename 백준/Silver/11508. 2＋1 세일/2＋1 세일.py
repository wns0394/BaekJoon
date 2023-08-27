n = int(input())

arr = []

for _ in range(n):
    c = int(input())
    arr.append(c)

arr.sort(reverse=True)

result = 0
for i in range(0, n, 3):
    if i + 1 < n:
        result += arr[i] + arr[i + 1]
    else:
        result += arr[i]
print(result)