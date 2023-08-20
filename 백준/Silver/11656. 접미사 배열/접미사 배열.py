arr = input()

result = []
for i in range(len(arr)):
    result.append(arr[i::])
result.sort()
for i in result:
    print(i)