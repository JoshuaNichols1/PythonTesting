inputf = open('input.txt', 'r')
outputf = open('output.txt', 'w')
a, ii, n, k = [], 0, 0, 0
for i in inputf:
    i = i.strip()
    a.append(i)
for i in a[0]:
    ii += 1
    if i != ' ':
        if ii == 1:
            n = int(i)
        else:
            k = int(i)
a.pop(0)
b, ii, num = [], 0, 0
for i in a[0]:
    if i != ' ':
        b.append(i)
print(b)
for i in b:
    i = int(i)
    b = b[:ii] + b[ii + 1:]
    print(b)
    for q in b:
        q = int(q)
        sum = (q + i)%k
        if sum == 0:
            num += 1
    ii += 1
print(num)