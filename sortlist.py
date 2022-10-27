from numpy import sort


b = input("")
a = []
for i in b.split():
    a.append(i)
a.sort()
line = ""
for i in a:
    line += f"{i} "
print(line)
