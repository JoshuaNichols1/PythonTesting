inputf = open('input.txt', 'r')
outputf = open('output.txt', 'w')
a = []
for i in inputf:
    i.strip()
    i = i.rstrip("\n")
    a.append(i)


def first2(x):
    prev, ii = '', 0
    for i in x[:2]:
        if ii == 1:
            prev += i
            if 12 < int(prev) < 24:
                k = int(prev) - 12
                x = str(k) + x[2:]
                if int(k) > 9:
                    return (x + 'pm')
                else:
                    return ('0' + x + 'pm')
            elif prev == '00':
                k = 12
                x = str(k) + x[2:]
                return (x + 'am')
            elif prev == '12':
                return (x + 'pm')
            else:
                return (x + 'am')
        else:
            prev += i
            ii += 1


def final(x):
    k = x[2] + x[3]
    c = x[0] + x[1]
    if int(k) > 59:
        return 'Invalid Time'
    elif int(c) > 13:
        return 'Invalid Time'
    elif int(c) > 9:
        x = x[:2] + ':' + x[2:4] + ' ' + x[4:]
        return x
    else:
        x = x[1:2] + ':' + x[2:4] + ' ' + x[4:]
        return x

for i in a:
    k = first2(i)
    kk = final(k)
    print(f'{i}    {kk}')
