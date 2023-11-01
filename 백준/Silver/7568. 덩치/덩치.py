n = int(input())

arr = []
for _ in range(n): 
    x,y = map(int,input().split())
    arr.append((x,y))


for i in range(n):
    a = arr[i][0]
    b = arr[i][1]
    count = 0
    for j in range(n):
        if a < arr[j][0] and b < arr[j][1]:
            count += 1

    print(count+1, end= ' ')