import random

firstf = open('first.txt', 'r')
lastf = open('last.txt', 'r')
outputf = open('output.txt', 'w')

amount = int(input('How many names should be generated? '))

f = []
l = []

for i in firstf:
    for line in i.split():
        f.append(line)

for i in lastf:
    for line in i.split():
        l.append(line[:-1])

for i in range(amount):
    if i != amount-1:
        outputf.write(f'{random.choice(f)} {random.choice(l)}\n')
    else:
        outputf.write(f'{random.choice(f)} {random.choice(l)}')