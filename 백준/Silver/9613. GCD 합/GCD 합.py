from itertools import combinations
from math import gcd

t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))

    n = a[0]
    arr = a[1::]
    all = list(combinations(arr,2))
    result = 0
    for i in all:
        x = i[0]
        y = i[1]
        result += gcd(x,y)
    print(result)