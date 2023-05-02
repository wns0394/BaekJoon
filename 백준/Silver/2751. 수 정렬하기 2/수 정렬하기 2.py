n = int(input())
arr = []
for _ in range(n):
    # a = int(input())
    arr.append(int(input()))

arr.sort(reverse=False)
for i in range(n):
    print(arr[i])