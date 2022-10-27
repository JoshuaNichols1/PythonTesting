inputf = open("input.txt", "r")
outputf = open("output.txt", "w")
lines = []
# for i in inputf:
#     i = i.strip()
#     word = i.split()
#     lines.append(word)
dictionary = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thriteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000,
    "billion": 1000000000,
    "trillion": 1000000000000,
    "plus": "+",
    "minus": "-",
    "times": "x",
}
ii = 0
final = []
for item in inputf:
    ii += 1
    item = item.strip()
    words = item.split()
    newline = ""
    done = 1
    num1 = 0
    num2 = 0
    upto = 0
    leng = len(words)
    i = 0
    for item in words:
        i += 1
        k = dictionary.get(item)
        if item == "and":
            newline += ""
        elif type(k) == int:
            if i == leng:
                if k > 90:
                    num2 += int(k * upto)
                else:
                    num2 += int(k)
                fin2 = num2 + upto
                newline += str(fin2) + " "
            if done > 0:
                if k > 90:
                    num1 += int(k * upto)
                    upto = 0
                else:
                    upto += k
            elif done == 0:
                if k > 90:
                    num2 += int(k * upto)
                    upto = 0
                else:
                    upto += k
        elif type(k) == str:
            done = 0
            fin = num1 + upto
            newline += str(fin) + " "
            newline += k + " "
            upto = 0
    # newline = [dictionary.get(item) for item in words]
    final.append(newline)
print("\n".join(final[:-1]))
