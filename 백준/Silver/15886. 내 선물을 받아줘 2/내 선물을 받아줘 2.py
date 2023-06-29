n = int(input())
arr = input()
count = 0
for i in range(n-1):
    if arr[i:i+2] == 'EW':
        count += 1

print(count)