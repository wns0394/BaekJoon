n = int(input())
arr = list(map(int,input().split()))
a = int(input())

def dfs(node,arr):
    # 지울노드를 -2로 변경
    arr[node] = -2

    for i in range(n):
        # 지워야 하는 노드를 부모로 둔 자식 노드일 경우, 자식 노드를 -2로 반환
        if arr[i] == node:
            dfs(i,arr)

dfs(a,arr)

leaf = 0
for i in range(n):
    # 부모노드가 -2가 아니고
    if arr[i] != -2:
        # 자신이 부모가 아니라면 -> 자식이 없다는 말
        if i not in arr:
            leaf += 1
print(leaf)