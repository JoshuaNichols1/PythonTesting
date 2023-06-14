import random
import math
import pyperclip as pc

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMS = "1234567890"
PUNC = """"'`~,./;[]-=!@#$%^&*()_+{}:<>?"""


def password(length=8, lower=LOWER, upper=UPPER, nums=NUMS, punc=PUNC):
    """
    For each character type do e.g. lower="" if you don't want lower case.
    Default password length is 8 characters.
    Length must be greater than 4.
    Password is copied to clipboard.
    """

    if length <= 4:
        print("The password length was either zero or a negative")
        return None

    all = LOWER + UPPER + NUMS + PUNC
    num = len(all)
    all = all * math.ceil(length / num)
    password = "".join(random.sample(all, length))
    pc.copy(password)
    return password


print(password(40))
