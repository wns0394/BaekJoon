import sys

input = sys.stdin.readline

from itertools import permutations, combinations

n = int(input())

arr = [int(i) for i in range(1,n+1)]

result = list(permutations(arr,n))

for i in result:
    print(*i)