inputf = open('input.txt', 'r')
outputf = open('output.txt', 'w')
a=[]
for line in inputf:
    for word in line.split():
        a.append(word)
g = a[0]
a.pop(0)
b = []
for i in range(len(a)):
    i += 1
    b.append(2 + (i-1)*5)
ii = 0
goodorig = []
justneeded = []
for i in a:
    ii += 1
    if ii not in b:
        goodorig.append(a[ii-1])
d = []
for i in range(len(goodorig)):
    i += 1
    d.append(3 + (i-1)*4)
ii = 0
for i in goodorig:
    ii += 1
    if ii not in d:
        justneeded.append(goodorig[ii-1])
f = []
for i in range(len(justneeded)):
    i += 1
    f.append(1 + (i-1)*3)
h = []
for i in range(len(justneeded)):
    i += 1
    h.append(2 + (i-1)*3)
j = []
for i in range(len(justneeded)):
    i += 1
    j.append(3 + (i-1)*3)
first = []
second = []
percent = []
ii = 0
for i in justneeded:
    ii += 1
    if ii in f:
        first.append(justneeded[ii-1])
ii = 0
for i in justneeded:
    ii += 1
    if ii in h:
        second.append(justneeded[ii-1])
ii = 0
for i in justneeded:
    ii += 1
    if ii in j:
        percent.append(justneeded[ii-1])
full = ''
ii = 0
for i in range(int(len(first))):
    x = first[i]
    y = second[i]
    z = percent[i]
    z = z[:-1]
    z = str(round(float(100)-float(z)))
    full += f'IF({g}>={x}, "{z} Percentile", '
outputf.write(full + '""' + (i+1)*')')