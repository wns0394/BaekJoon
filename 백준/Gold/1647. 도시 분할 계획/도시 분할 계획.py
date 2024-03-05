import sys

input = sys.stdin.readline


# find 함수
def find(parent, x):
    # 노드 x의 부모노드가 자기자신이 아니면
    if parent[x] != x:
        # 루트노드를 찾을때까지 반복
        parent[x] = find(parent, parent[x])
    return parent[x]


# union 함수
def union(parent, a, b):
    # a와 b의 루트노드 탐색
    a = find(parent, a)
    b = find(parent, b)

    # 작은 노드를 부모로 갱신
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 집의 개수 n, 길의 개수 m
n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

# 모든 도로에 대한 정보
street = []

for _ in range(m):
    # a번 집과 b번 집을 연결하는 비용 c
    a, b, c = map(int, input().split())
    street.append((c, a, b))

# 비용순으로 정렬
street.sort()

result = 0

# 두개의 마을로 분리하기 때문에
# 가장 마지막에 최소 신장트리를 만족하는 비용을 제거하면 최소 금액이 된다
max_cost = 0
for i in street:
    c, a, b = i

    # 싸이클이 발생하지 않는 경우
    # 즉 최소신장트리를 만족한다
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c
        max_cost = c

print(result - max_cost)
