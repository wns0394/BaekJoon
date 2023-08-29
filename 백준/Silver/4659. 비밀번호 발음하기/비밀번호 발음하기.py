
while True:
    word = input()
    if word == 'end':
        break
    wordlist = list(word)

    mo = 0

    mocount = 0
    jacount = 0

    err = 0

    molist = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(wordlist)):
        if i > 0:
            if wordlist[i] == wordlist[i - 1] and wordlist[i] != 'e' and wordlist[i] != 'o':
                err = 1
                break
        if wordlist[i] in molist:
            mo = 1
            mocount += 1
            jacount = 0

            if mocount == 3:
                err = 1
                break
        else:
            mocount = 0
            jacount += 1

            if jacount == 3:
                err = 1
                break
    if err == 1 or mo == 0:
        print(f'<{word}> is not acceptable.')
    else:
        print(f'<{word}> is acceptable.')
