start = 10000
final = 0
dividend = 0
i = 0
while dividend < 100000:
    if i < 6:
        while i < 6 or dividend < 100000:
            i += 1
            final += 3000
            dividend += (final * 0.1)
            final += dividend
    elif i < 10:
        while i < 10 or dividend < 100000:
            i += 1
            final += start
            dividend += (final * 0.1)
            final += dividend
    elif 10 < i:
        while dividend < 100000:
            i += 1
            final += 15000
            dividend += (final * 0.1)
            final += dividend
else:
    print(i, round(dividend, 0), round(final, 0))
