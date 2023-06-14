def add_subtract(type_eq="add"):
    coefficient = 1
    if type_eq == "subtract":
        coefficient = -1
    vals = input(f"Enter numbers to {type_eq} (separated by spaces): ")
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


def times_divide(type_eq=["multiply", "*"]):
    vals = input(f"Enter numbers to {type_eq[0]} (separated by spaces): ")
    num = 0
    total = 1
    for i in vals.split():
        try:
            if num == 0:
                if type_eq[1] == "/":
                    total = float(i)
            else:
                total = eval(f"total {type_eq[1]} float(i)")
            num += 1
        except:
            print(
                f"Input {num+1} was invalid so was not included in calculation."
            )
    return total


choices = {
    "1": """add_subtract()""",
    "2": """add_subtract(type_eq="subtract")""",
    "3": """times_divide()""",
    "4": """times_divide(["divide","/"])""",
}
choice = input(
    "What sum type is required (1 for +, 2 for -, 3 for x, 4 for /)? "
)
try:
    print(eval(choices[choice]))
except KeyError:
    print("Invalid sum type. Please restart program.")
