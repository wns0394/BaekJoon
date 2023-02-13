
from collections import deque

arr = list(map(str,input()))
list = []
cnt = 1
result = 0
for i in range(len(arr)):
    a = arr[i]

    if a == '(':
        cnt *= 2
        list.append(a)

    elif a == '[':
        cnt *= 3
        list.append(a)

    elif a == ')':
        if len(list) == 0 or list[-1] == '[':
            result = 0
            break
        if arr[i-1] == '(':
            result += cnt
        cnt //= 2
        list.pop()
    else:
        if len(list) == 0 or list[-1] == '(':
            result = 0
            break
        if arr[i-1] == '[':
            result += cnt
        cnt //= 3
        list.pop()

if list:
    result = 0
print(result)

