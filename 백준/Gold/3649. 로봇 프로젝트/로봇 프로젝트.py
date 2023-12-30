# 1센티미터 = 10000000 나노미터

while True:
    try:
        # 구멍의 너비
        x = int(input())

        # 레고 조각의 수
        n = int(input())

        arr = []
        for _ in range(n):
            # 레고 조각의 길이 l 나노미터
            l = int(input())
            arr.append(l)

        arr.sort()

        s = 0
        e = n-1
        flag = False
        while s < e:
            if arr[s] + arr[e] == x * 10000000:
                print('yes',arr[s],arr[e])
                flag = True
                break
            elif arr[s] + arr[e] < x * 10000000:
                s += 1
            else:
                e -= 1
        if flag == False:
            print('danger')
    except:
        break