import sys

input = sys.stdin.readline

from itertools import permutations

# n의 개수는 8이 최대
# 가능한 경우의 수 8! = 40320개
# 거기서 또 8개의 반복을 돌아야하니까 32만개
# 시간초과는 안남

n = int(input())
arr = list(map(int, input().split()))

all_case = list(set(permutations(arr, n)))

result = 0

for i in range(len(all_case)):
    count = 0
    for j in range(n - 1):
        count += abs(all_case[i][j] - all_case[i][j + 1])

    if count > result:
        result = count

print(result)
