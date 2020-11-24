import math

def give(givens):
    a, g = [], givens.split()
    for i in g:
        a.append(i)
    return a


def needshalf(t, x, xo):
    answer = (math.log2(x/xo))*float(t)
    answer = answer * float(-1)
    return answer


def needst(half, x, xo):
    answer = (math.log2(x/xo))*float(half)
    answer = answer * float(-1)
    return answer


def needsx(half, t, xo):
    answer = float(xo)*(1/2) ** (t/half)
    return answer


def needsxo(half, t, x):
    answer = float(x)/((1/2) ** (t/half))
    return answer

def halftime(half, time, X, Xo):
    if half == '?':
        answer = needshalf(float(time), float(X), float(Xo))
        return (f'Half-Life = {answer}')
    elif time == '?':
        answer = needst(float(half), float(X), float(Xo))
        return (f'Time = {answer}')

def main(Type):
    Type = input('What Type (A, N, M)? ')
    Givens = input(
        'Givens (order: t 1/2, t, X, Xo. If haven\'t got then put in ?) ')
    a = give(Givens)
    half, time, X, Xo = a[0], a[1], a[2], a[3]
    if Type == 'A':
        if half == '?':
            return halftime(half, time, X, Xo)
        elif time == '?':
            return halftime(half, time, X, Xo)
        elif X == '?':
            answer = needsx(float(half), float(time), float(Xo))
            return (f'Activity = {answer}')
        elif Xo == '?':
            answer = needsxo(float(half), float(time), float(X))
            return (f'Original Activity = {answer}')
    elif Type == 'N':
        if half == '?':
            return halftime(half, time, X, Xo)
        elif time == '?':
            return halftime(half, time, X, Xo)
        elif X == '?':
            answer = needsx(float(half), float(time), float(Xo))
            return (f'Number of Nuclei = {answer}')
        else:
            answer = needsxo(float(half), float(time), float(X))
            return (f'Original Number of Nuclei = {answer}')
    elif Type == 'M':
        if half == '?':
            return halftime(half, time, X, Xo)
        elif time == '?':
            return halftime(half, time, X, Xo)
        elif X == '?':
            answer = needsx(float(half), float(time), float(Xo))
            return (f'Mass = {answer}')
        else:
            answer = needsxo(float(half), float(time), float(X))
            return (f'Original Mass = {answer}')
