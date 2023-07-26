cont = True
while cont:
    try:
        binary = str(input("Enter a binary number: "))
        sum = 0
        for num, digit in enumerate(binary):
            if int(digit) > 1:
                raise ValueError
            sum += int(digit) * 2 ** (len(binary) - 1 - num)
        print(sum)
    except:
        continue
