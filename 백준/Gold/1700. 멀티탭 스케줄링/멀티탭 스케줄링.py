from collections import deque


n,k = map(int,input().split())

arr = list(map(int,input().split()))

new = deque()
new.append(arr[0])

for i in range(1,k):
    if new[-1] != arr[i]:
        new.append(arr[i])

tap = deque()
while True:
    tap.append(new.popleft())
    if len(tap) == n:
        break

while new and new[0] in tap:
    new.popleft()
count = 0
while new:
    # last_index[0] : 값
    # last_index[1] : 어떤 숫자인지
    last_index = [0,0]
    for i in tap:
        if i in new and new.index(i) > last_index[0]:
            last_index[0] = new.index(i)
            last_index[1] = i
        if i not in new:
            last_index[0] = 0
            last_index[1] = i
            break
    tap.remove(last_index[1])
    tap.append(new.popleft())
    count += 1
    while new and new[0] in tap:
        new.popleft()

print(count)