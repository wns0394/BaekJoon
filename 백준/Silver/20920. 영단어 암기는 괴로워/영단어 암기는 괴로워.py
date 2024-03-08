import sys

input = sys.stdin.readline

from collections import defaultdict

n, m = map(int, input().split())

dict = defaultdict(int)

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        dict[word] += 1

result = list(dict)
result.sort(key=lambda x: (-dict[x], -len(x), x))

for i in result:
    print(i)
