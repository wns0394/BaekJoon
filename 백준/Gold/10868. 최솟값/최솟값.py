import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [int(input()) for i in range(n)]

h = int(math.ceil(math.log2(n))) + 1

tree = [0] * (2 ** h)


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    # 좌측 노드와 우측 노드 중 작은거 선택.
    tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))
    return tree[index]


init(0, n - 1, 1)


def search(start, end, index, left, right):
    if left > end or right < start:
        return 1000000001
    if left <= start and right >= end:
        return tree[index]

    mid = (start + end) // 2
    return min(search(start, mid, index * 2, left, right), search(mid + 1, end, index * 2 + 1, left, right))


for _ in range(m):
    a, b = map(int, input().split())
    print(search(0, n - 1, 1, a-1, b-1))
