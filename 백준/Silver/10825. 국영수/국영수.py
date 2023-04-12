
n = int(input())

list = []
for _ in range(n):
    list.append(input().split())
arr = sorted(list, key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
# print(sorted(list, key=lambda x : (-int(x[1]),x[2],-int(x[3]),x[0])))

for i in arr:
    print(i[0])