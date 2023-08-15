import math

# unsigned binary to number


def unsigned_binary_to_num(binary):
    try:
        sum = 0
        for num, digit in enumerate(binary):
            if int(digit) > 1:
                raise ValueError
            sum += int(digit) * 2 ** (len(binary) - 1 - num)
        return sum
    except ValueError as e:
        return e


# signed binary to number


def signed_binary_to_num(binary: str):
    sign = 1
    if binary[0] == "1":
        binary = binary[1:]
        sign = -1
    return sign * unsigned_binary_to_num(binary)


# binary to octal


def binary_to_octal(binary: str):
    n = 3
    binary = (len(binary) % n * n - len(binary)) * "0" + binary
    binary = [binary[i : i + n] for i in range(0, len(binary), n)]
    octal = ""
    for group in binary:
        octal += str(unsigned_binary_to_num(group))
    return int(octal)


# binary to hexadecimal


def binary_to_hexa(binary: str):
    n = 4
    print(math.ceil(len(binary) / n) - len(binary))
    binary = (math.ceil(len(binary) / n) - len(binary)) * "0" + binary
    binary = [binary[i : i + n] for i in range(0, len(binary), n)]
    hexa = ""
    print(binary)
    hexa_convert = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    for group in binary:
        group_sum = str(unsigned_binary_to_num(group))
        if int(group_sum) > 9:
            group_sum = hexa_convert[int(group_sum)]
        hexa += group_sum
    return int(hexa)


# print(binary_to_octal("10001"))
print(binary_to_hexa("10001"))
