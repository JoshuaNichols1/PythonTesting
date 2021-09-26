type = input("What sum type is required (1 for +, 2 for -, 3 for x, 4 for /)? ")


def add():
    numbers = input("Enter values for sum seperated by a space in intended order. ")
    n = []
    maxD = 0
    for i in numbers.split():
        amount = i[::-1].find(".")
        if amount > maxD:
            maxD = amount
        n.append(float(i))
    total = 0
    for i in n:
        total += i
    if maxD == 0:
        print(int(total))
    else:
        print(round(total, maxD))


def minus():
    numbers = input("Enter values for sum seperated by a space in intended order. ")
    n = []
    maxD = 0
    for i in numbers.split():
        amount = i[::-1].find(".")
        if amount > maxD:
            maxD = amount
        n.append(float(i))
    total = 0
    ii = 0
    for i in n:
        ii += 1
        if ii == 1:
            total = i
        else:
            total -= i
    if maxD == 0:
        print(int(total))
    else:
        print(round(total, maxD))


def times():
    numbers = input("Enter values for sum seperated by a space in intended order. ")
    n = []
    maxD = 0
    for i in numbers.split():
        amount = i[::-1].find(".")
        if amount > maxD:
            maxD = amount
        n.append(float(i))
    total = 0
    ii = 0
    for i in n:
        ii += 1
        if ii == 1:
            total = i
        else:
            total *= i
    if maxD == 0:
        print(int(total))
    else:
        print(round(total, maxD))


def divide():
    numbers = input("Enter values for sum seperated by a space in intended order. ")
    n = []
    maxD = 0
    for i in numbers.split():
        amount1 = i[::-1].find(".")
        if amount1 > maxD:
            maxD = amount1
        n.append(float(i))
    total = 0
    ii = 0
    for i in n:
        ii += 1
        if ii == 1:
            total = i
        else:
            total /= i
    amount = str(total)[::-1].find(".")
    if amount > maxD:
        choice = input(
            f"The amount of decimal places for the answer is {amount}, please enter amount of decimal places wanted. "
        )
        try:
            choice = int(choice)
            if choice <= amount:
                print(round(total, int(choice)))
            else:
                print(
                    "Inputted decimal places are invalid, here is the unrounded number:"
                )
                print(total)
        except ValueError:
            print("Inputted decimal places are invalid, here is the unrounded number:")
            print(total)
    else:
        print(total)


if type == "1":
    add()
elif type == "2":
    minus()
elif type == "3":
    times()
elif type == "4":
    divide()
else:
    print("Invalid sum type. Please restart program.")
