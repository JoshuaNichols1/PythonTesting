def add_subtract(minus="add"):
    coefficient = 1
    if minus == "subtract":
        coefficient = -1
    vals = input(f"Enter numbers to {minus} (separated by spaces): ")
    total = 0
    num = 0
    for i in vals.split():
        try:
            if num != 0:
                total += coefficient * float(i)
            else:
                total += float(i)
            num += 1
        except:
            print(
                f"Input {num+1} was invalid so was not included in calculation."
            )

    return total


def times():
    vals = input(f"Enter numbers to multiply (separated by spaces): ")
    total = 1
    num = 0
    for i in vals.split():
        try:
            total *= float(i)
            num += 1
        except:
            print(
                f"Input {num+1} was invalid so was not included in calculation."
            )
    return total


def divide():
    vals = input(f"Enter numbers to multiply (separated by spaces): ")
    total = 1
    num = 0
    for i in vals.split():
        try:
            if num == 0:
                total = float(i)
            else:
                total /= float(i)
            num += 1
        except:
            print(
                f"Input {num+1} was invalid so was not included in calculation."
            )
    return total


choices = {
    "1": """add_subtract()""",
    "2": """add_subtract(minus="subtract")""",
    "3": """times()""",
    "4": """divide()""",
}
choice = input(
    "What sum type is required (1 for +, 2 for -, 3 for x, 4 for /)? "
)
try:
    print(eval(choices[choice]))
except KeyError:
    print("Invalid sum type. Please restart program.")
