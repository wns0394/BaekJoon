import sys

input = sys.stdin.readline

n = int(input())

result = []

arr = []
def dfs():
    
    if arr:
        result.append(int(''.join(map(str,arr))))
        
    for i in range(10):
        if len(arr) == 0 or arr[-1] > i:
            arr.append(i)
            dfs()
            arr.pop()
dfs()

result.sort()

try:
    print(result[n-1])
except:
    print(-1)
