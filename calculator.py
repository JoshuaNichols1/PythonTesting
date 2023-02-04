def process_input_values():
    numbers = input("Enter values for sum separated by a space in intended order: ")
    n = []
    maxD = 0
    for i in numbers.split():
        amount = i[::-1].find(".")
        if amount > maxD:
            maxD = amount
        n.append(float(i))
    return n, maxD

def perform_operation(n, maxD, operation):
    total = 0
    ii = 0
    for i in n:
        ii += 1
        if ii == 1:
            total = i
        else:
            total = operation(total, i)
    if maxD == 0:
        return int(total)
    else:
        return round(total, maxD)

def add(total, i):
    return total + i

def minus(total, i):
    return total - i

def times(total, i):
    return total * i

def divide(total, i):
    return total / i

def handle_division_result(total, maxD):
    amount = str(total)[::-1].find(".")
    if amount > maxD:
        choice = input(f"The amount of decimal places for the answer is {amount}, please enter amount of decimal places wanted: ")
        try:
            choice = int(choice)
            if choice <= amount:
                return round(total, choice)
            else:
                print("Inputted decimal places are invalid, here is the unrounded number:")
                return total
        except ValueError:
            print("Inputted decimal places are invalid, here is the unrounded number:")
            return total
    else:
        return total

type = input("What sum type is required (1 for +, 2 for -, 3 for x, 4 for /)? ")

if type == "1":
    n, maxD = process_input_values()
    result = perform_operation(n, maxD, add)
    print(result)

elif type == "2":
    n, maxD = process_input_values()
    result = perform_operation(n, maxD, minus)
    print(result)

elif type == "3":
    n, maxD = process_input_values()
    result = perform_operation(n, maxD, times)
    print(result)

elif type == "4":
    n, maxD = process_input_values()
    result = perform_operation(n, maxD, divide)
    result = handle_division_result(result, maxD)
    print(result)

else:
    print("Invalid sum type. Please restart program.")
