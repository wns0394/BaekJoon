
from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = [int(i) for i in range(1, n + 1)]
result = list(combinations_with_replacement(arr,m))
for i in result:
    print(*i)