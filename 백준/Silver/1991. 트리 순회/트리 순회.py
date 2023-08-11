import sys

n = int(input())

tree = {}
for _ in range(n):
    parent, left, right = map(str, input().split())
    tree[parent] = [left,right]


def left(parent):
    if parent != '.':
        print(parent, end='')
        left(tree[parent][0]) # 왼쪽
        left(tree[parent][1]) # 오른쪽
def mid(parent):
    if parent != '.':
        mid(tree[parent][0])  # 왼쪽
        print(parent, end='')
        mid(tree[parent][1])  # 오른쪽

def right(parent):
    if parent != '.':
        right(tree[parent][0])  # 왼쪽
        right(tree[parent][1])  # 오른쪽
        print(parent, end='')
left('A')
print()
mid('A')
print()
right('A')