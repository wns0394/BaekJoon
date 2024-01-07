import sys

input = sys.stdin.readline

# 친구들이 받고 싶어하는 사탕의 개수의 합은 항상 m을 넘는다
# 무조건 나머지가 생긴다.
# 나머지를 분노의 합이 최소가 되도록 나누려면
# 최대한 공평하게 나누어야 무조건적으로 최소가 된다.
# n빵은 불가능
# n빵 계산과 받고 싶어하는 것 중 작은것을 고르면 최소가 된다


m,n = map(int,input().split())

arr = []

for _ in range(n):
    candy = int(input())
    arr.append(candy)

arr.sort()

# 못 받은 사탕 수
na = sum(arr) - m

# 분노의 합
result = 0

for i in range(n):
    # 받고 싶어하는 사탕의 수 와 남은 분노를 남은 사람수로 n빵하는것과 비교
    # 작은것을 택한다
    a = min(arr[i], na // (n-i))

    # 분노 더해주기
    result += a**2

    # 나머지에서 a만큼 빼준다.
    na -= a

print(result % 2**64)
