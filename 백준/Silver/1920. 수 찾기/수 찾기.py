
n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

arr1.sort()

for number in arr2:
    start, end = 0, n-1
    isend = False
    while start <= end:
        mid = (start+end) // 2
        if number == arr1[mid]:
            isend = True
            print(1)
            break
        elif number > arr1[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if not isend:
        print(0)