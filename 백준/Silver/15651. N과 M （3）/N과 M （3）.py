from itertools import product

n, m = map(int, input().split())
arr = [int(i) for i in range(1, n + 1)]
# print(arr)
result = list(product(arr,repeat=m))
for i in result:
    print(*i)