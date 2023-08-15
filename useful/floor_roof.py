def floor(num):
    if int(num) > num:
        return int(num - 1)
    return int(num)


def roof(num):
    if int(num) < num:
        return int(num + 1)
    return int(num)
