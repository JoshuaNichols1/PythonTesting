import random
import math
import pyperclip as pc

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
punc = "`~,./;[]-=!@#$%^&*()_+{}:<>?"

length = int(input("What password length do you want? "))

if length <= 0:
    print("The password length was either zero or a negative")
else:
    qlower = input(
        'Include Lowercase letters (Leave blank for no, use "Y" for yes)? '
    )
    qupper = input(
        'Include Uppercase letters (Leave blank for no, use "Y" for yes)? '
    )
    qnums = input('Include Numbers (Leave blank for no, use "Y" for yes)? ')
    qpunc = input(
        'Include Punctuation (Leave blank for no, use "Y" for yes)? '
    )

    if qlower != "Y":
        lower = ""
    if qupper != "Y":
        upper = ""
    if qnums != "Y":
        nums = ""
    if qpunc != "Y":
        punc = ""

    all = lower + upper + nums + punc
    num = len(all)

    if num == 0:
        print("You included no character types in password")
    else:
        all = all * math.ceil(length / num)
        password = "".join(random.sample(all, length))
        pc.copy(password)
