inputf = open('input.txt', 'r')
outputf = open('output.txt', 'w')
a=[]
for line in inputf:
    for word in line.split():
        a.append(word)
# ii = 0
# for i in a:
#     ii += 1
#     if ((ii-2)/4+1).is_integer():
#         a.pop(ii-1)
# print(a)
b = []
d = []
for i in range(len(a)):
    i += 1
    b.append(2 + (i-1)*3)
for i in range(len(a)):
    i += 1
    d.append(2 + (i-1)*2)
ii = 0
# for i in a:
#     ii += 1
#     if ii in b:
#         a.pop(ii-1)
g = a[0]
a.pop(0)
c = []
e = []
f = []
for i in a:
    ii += 1
    if ii not in b:
        c.append(a[ii-1])
ii = 0
for i in c:
    ii += 1
    if ii not in d:
        e.append(c[ii])
ii = 0
for i in c:
    ii += 1
    if ii not in d:
        f.append(c[ii-1])
# ii = 0
# for i in a:
#     ii += 1
#     if ((ii-2)/3+1).is_integer():
#         a.pop(ii-1)
# print(a)
full = ''
ii = 0
for i in range(int(len(e))):
    x = f[i]
    z = e[i]
    z = z[:-1]
    z = str(float(100)-float(z))
    full += f'IF({g}={x}, "{z} Percentile", '
outputf.write(full + '""' + (i+1)*')')