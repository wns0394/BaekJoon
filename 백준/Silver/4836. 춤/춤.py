import sys

for a in sys.stdin:
    arr = list(map(str, a.split()))
    error = []
    if 'dip' not in arr:
        error.append(5)
    for i in range(len(arr)):
        if arr[i] == "dip":
            if i >= 2 and (arr[i - 1] == 'jiggle' or arr[i - 2] == 'jiggle'):
                continue
            if i >= 1 and arr[i-1] == 'jiggle':
                continue
            if i + 1 < len(arr) and arr[i + 1] == 'twirl':
                continue
            else:
                error.append(1)
                arr[i] = 'DIP'
    if arr[-3::] != ['clap', 'stomp', 'clap']:
        error.append(2)
    if 'twirl' in arr:
        if 'hop' not in arr:
            error.append(3)
    if arr[0] == 'jiggle':
        error.append(4)
    error.sort()
    if len(error) == 1:
        print(f'form error {error[0]}: {" ".join(arr)}')
    elif len(error) == 2:
        print(f'form errors {error[0]} and {error[-1]}: {" ".join(arr)}')
    elif len(error) > 2:
        print('form errors', end=' ')
        for i in range(len(error)):
            if i < len(error) - 2:
                print(error[i], end=', ')
            elif i < len(error) - 1:
                print(error[i], end='')
            else:
                print(f' and {error[i]}: {" ".join(arr)}')
    else:
        print('form ok:', *arr)
