inputf, outputf, a, ii = open('input.txt', 'r'), open('output.txt', 'w'), [], 1

for i in inputf:
    if ii == 1:
        i, ii = i.strip('\n').strip(), 0
        i = str(i)
        a.append(i)
    else:
        ii = 1
q = a[-1]
a.pop(-1)
a2 = a
dictionary = {
    'a': '2',
    'b': '2',
    'c': '2',
    'd': '3',
    'e': '3',
    'f': '3',
    'g': '4',
    'h': '4',
    'i': '4',
    'j': '5',
    'k': '5',
    'l': '5',
    'm': '6',
    'n': '6',
    'o': '6',
    'p': '7',
    'q': '7',
    'r': '7',
    's': '7',
    't': '8',
    'u': '8',
    'v': '8',
    'w': '9',
    'x': '9',
    'y': '9',
    'z': '9',
    ' ': '#',
    '\'': ''
}

curr, ii, new = '', 0, ''

for word in a2:
    for letter in word:
        new = dictionary.get(letter)
        curr += new
    a2[ii] = curr
    ii += 1
    curr , new = '', ''
word, prev, possible, ii = '', '', [], 0
for k in q:
    ii += 1
    if k == '#':
        if prev in a2:
            for i, j in enumerate(a2):
                if j == prev:
                    possible.append(i)
            for i in possible:
                word += f'{a[i]} '
        else:
            word += '??? '
        prev = ''
    elif ii == len(q):
        if prev in a2:
            prev += k
            for i, j in enumerate(a2):
                print(i, j)
                if j == prev:
                    possible.append(i)
            for i in possible:
                word += f'{a.index(i)}'
        else:
            word += '???'
    else:
        prev += k
print(word)