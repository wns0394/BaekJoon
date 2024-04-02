import sys
input = sys.stdin.readline

# index를 담을 first set()와
# 숫자를 담을 second set()와
# index x
def dfs(first, second, x):
    # first set에 index x 담아주기
    first.add(x)
    # second set에 arr[x] 담아주기
    second.add(arr[x])

    # arr[x]가 first set에 있다면
    if arr[x] in first:
        # fisrt와 second가 같다면
        if first == second:
            # result 업데이트
            result.update(first)
            return True
        return False
    # 아니라면 arr[x]값에 대한 dfs 실행
    return dfs(first,second,arr[x])


n = int(input())

arr = [0]

for _ in range(n):
    t = int(input())
    arr.append(t)

result = set()

for i in range(1, n + 1):
    # i가 result에 없을때만 dfs 실행
    if i not in result:
        # print(i)
        dfs(set(),set(),i)

print(len(result))
result = list(result)
for i in sorted(result):
    print(i)
