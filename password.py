import random
import math

outputf = open('output.txt', 'w')

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '1234567890'
punc = '`~,./;[]-=!@#$%^&*()_+{}:<>?'

length = int(input('What password length do you want? '))

if length <= 0:
    outputf.write('The password length was either zero or a negative')
else:
    qlower = input('Include Lowercase letters (Leave blank for no, use "Y" for yes)?')
    qupper = input('Include Uppercase letters (Leave blank for no, use "Y" for yes)?')
    qnums = input('Include numbers (Leave blank for no, use "Y" for yes)?')
    qpunc = input('Include Punctuation (Leave blank for no, use "Y" for yes)?')

    if qpunc != "Y":
        punc = ''
    if qlower != "Y":
        lower = ''
    if qupper != "Y":
        upper = ''
    if qnums != "Y":
        nums = ''

    all = lower + upper + nums + punc
    num = len(lower)+len(upper)+len(nums)+len(punc)

    if num == 0:
        outputf.write('You included no character types in password')
    else:
        all = all * math.ceil(length/num)
        password = "".join(random.sample(all, length))
        outputf.write(password)
# if length > 90:
#     length = 90
#     outputf.write("Your password length is too high, this has been adjusted to the max value of 90 characters \n")