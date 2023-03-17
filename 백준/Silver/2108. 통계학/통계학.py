
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
# 최빈값
count = dict()
for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
# print(count)

c = 0
result = []
for i, cnt in list(count.items()):
    if cnt > c:
        result = [i]
        c = cnt
    elif cnt == c:
        result.append(i)
result.sort()

# print(result)


print(round(sum(arr)/n))
print(sorted(arr)[n//2])
if len(result) == 1:
    print(result[0])
else:
    print(result[1])
print(max(arr)-min(arr))