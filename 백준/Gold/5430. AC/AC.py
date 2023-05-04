t = int(input())
for _ in range(t):
    p = list(input())
    n = int(input())
    arr = input()
    flip = 1
    if n == 0 and 'D' in p:
        result = 'error'
    elif n == 0 and 'R' in p:
        result = '[]'
    else:

        arr1 = list(map(int, arr[1:-1].split(',')))
        for i in range(len(p)):
            if p[i] == 'R':
                flip = -flip
            elif p[i] == 'D' and len(arr1) != 0:
                if flip == 1:
                    arr1.pop(0)
                else:
                    arr1.pop(-1)
            elif p[i] == 'D' and len(arr1) == 0:
                arr1 = 'error'
                break
        result = arr1

    if result != 'error' and len(result) != 0 and flip == -1:

        print("[" + ",".join(list(map(str, result[::-1]))) + "]")
    elif result != 'error' and result != '[]':
        # print(result, 'zzz')

        print("[" + ",".join(list(map(str, result))) + "]")
    else:
        print(result)