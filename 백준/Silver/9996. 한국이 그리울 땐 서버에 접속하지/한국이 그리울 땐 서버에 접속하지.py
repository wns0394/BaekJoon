n = int(input())
pattern = input().split('*')

left = pattern[0]
right = pattern[1]
for _ in range(n):
    word = input()
    if len(left) + len(right) > len(word):
        print('NE')
    else:
        if word[:len(left)] == left and word[-len(right):] == right:
            print('DA')
        else:
            print('NE')