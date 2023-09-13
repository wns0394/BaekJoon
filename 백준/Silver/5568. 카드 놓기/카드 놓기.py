from itertools import permutations

n = int(input())
k = int(input())

arr = []
for _ in range(n):
    a = str(input())
    arr.append(a)

result = set()
for i in permutations(arr,k):
    result.add(''.join(i))
print(len(result))