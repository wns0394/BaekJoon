import sys

from pprint import pprint

input = sys.stdin.readline

while True:
    arr = list(input().rstrip())

    a = list(reversed(arr))

    if arr == ['0']:
        break

    if a == arr:
        print('yes')
    else:
        print('no')