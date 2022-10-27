import random, math

i = 0
numbers = {}
printed = {}
prev_printed = 0

while i < pow(2, 20):
    i += 1
    min_i = i - 1
    n = i
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        steps += 1
    numbers[f"Number {i}"] = steps
    if i == 1:
        printed[f"Number {i}"] = steps
        prev_printed = steps
    elif steps > prev_printed:
        printed[f"Number {i}"] = steps
        prev_printed = steps

print(printed)
