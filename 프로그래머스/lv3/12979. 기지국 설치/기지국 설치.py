def solution(n, stations, w):
    answer = 0
#     arr = [0 for _ in range(n)]
#     for i in stations:
#         if i-1-w >= 0 and i+w < n:
#             arr[i-1-w:i+w] = [1] * (2*w+1)
#         elif i-1-w < 0:
#             arr[0:i+w] = [1] * (i+w)
#         elif i+w >= n:
#             arr[i-1-w::] = [1] * (n-i+1+w)
#     print(arr)
    
#     count = 0
#     distance = 0
#     for i in range(n):
#         if arr[i] == 0:
#             distance += 1
#         if i == n-1 and arr[i] == 0:
#             if distance % (2*w+1) == 0:
#                 count += distance // (2*w+1)
#             else:
#                 count += distance // (2*w+1) + 1
#         elif arr[i] == 1:
#             if distance % (2*w+1) == 0:
#                 count += distance // (2*w+1)
#             else:
#                 count += distance // (2*w+1) + 1
#             distance = 0
#     answer = count

    start = 1
    for i in stations:
        end = i - w
        distance = end-start
        if distance % (2*w+1) == 0:
            answer += distance // (2*w+1)
        else:
            answer += distance // (2*w+1) + 1
        
        start = i + w + 1
    if start <= n:
        distance = n-start+1
        if distance % (2*w+1) == 0:
            answer += distance // (2*w+1)
        else:
            answer += distance // (2*w+1) + 1
    return answer