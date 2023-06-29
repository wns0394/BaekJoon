
arr = list(input())

# 중간에 펠린드롬인거 찾기!
for i in range(len(arr)):
    # i번째부터 펠린드롬이면
    if arr[i:] == arr[i:][::-1]:
        # arr길이에 i 만큼 더해준다
        print(len(arr) + i)
        break