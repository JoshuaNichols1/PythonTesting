import math


def give(givens):
    a = []
    g = givens.split()
    for i in g:
        a.append(i)
    return a


def disvel(a, b, c, type):
    if a == '?':
        answer = float(b)/float(c)
        if type == 'dis':
            return 'Displacement', answer
        else:
            return 'Velocity', answer
    elif b == '?':
        answer = float(a)*float(c)
        if type == 'dis':
            return 'Distance', answer
        else:
            return 'Displacement', answer
    elif c == '?':
        answer = float(b)/float(a)
        return 'Time', answer


def eq1(a, b, c, d):
    if a == '?':
        answer = float(b) + (float(c)*float(d))
        return 'Velocity', answer
    elif b == '?':
        answer = float(a) - (float(c)*float(d))
        return 'Initial Velocity', answer
    elif c == '?':
        answer = (float(a) - float(b))/float(d)
        return 'Acceleration', answer
    elif d == '?':
        try:
            answer = (float(a) - float(b))/float(c)
            return 'Time', answer
        except answer < 0:
            answer = (float(a) - float(b))/float(c)
            return 'Time', answer * float(-1)


def eq2(a, b, c, d):
    if a == '?':
        answer = float(b)*float(d) + (1/2)*float(c)*float(d)**2
        return 'Displacement', answer
    elif b == '?':
        answer = (float(a) - (1/2)*float(c)*float(d)**2)/float(d)
        return 'Initial Velocity', answer
    elif c == '?':
        answer = (float(a) - float(b)*float(d))/((1/2)*float(d)**2)
        return 'Acceleration', answer
    elif d == '?':
        try:
            answer = (-float(b)+ math.sqrt(float(b)**2+float(2)*float(c)*float(a)))/float(c)
            if answer < 0:
                return 'Time', answer*float(-1)
            else:
                return 'Time', answer
        except ValueError:
            return 'no'


def eq3(a, b, c, d):
    if a == '?':
        try:
            answer = math.sqrt(float(b)**2 + float(2)*float(c)*float(d))
            return 'Velocity', answer
        except ValueError:
            return 'no'
    elif b == '?':
        try:
            answer = math.sqrt(float(a)**2 - float(2)*float(c)*float(d))
            return 'Initial Velocity', answer
        except ValueError:
            return 'no'
    elif c == '?':
        answer = (float(a)**2 - float(b)**2)/2*float(d)
        return 'Acceleration', answer
    elif d == '?':
        answer = (float(a)**2 - float(b)**2)/2*float(c)
        return 'Displacement', answer


def eq4(a, b, c, d):
    if a == '?':
        answer = (float(b) - float(c))/float(d)
        return 'Acceleration', answer
    elif b == '?':
        answer = float(a)*float(d) - float(c)
        return 'Velocity', answer
    elif c == '?':
        answer = float(c) - float(a)*float(d)
        return 'Initial Velocity', answer
    elif d == '?':
        try:
            answer = (float(b) - float(c))/float(a)
            return 'Time', answer
        except answer < 0:
            answer = (float(b) - float(c))/float(a)
            return 'Time', answer*float(-1)

def main(Type):
    if Type == 'ds':
        which = input('Which equation (Displacement (d) or Velocity (v) )? ')
        if which == 'd':
            Givens = input(
                'Givens (order: s d t. If haven\'t got then put in ?): ')
            a = give(Givens)
            s, d, t = a[0], a[1], a[2]
            answer = disvel(s, d, t, 'dis')
            var, answer = answer[0], answer[1]
            return (f'{var} = {answer}')
        elif which == 'v':
            Givens = input(
                'Givens (order: v s t. If haven\'t got then put in ?): ')
            a = give(Givens)
            v, s, t = a[0], a[1], a[2]
            answer = disvel(v, s, t, 'vel')
            var, answer = answer[0], answer[1]
            return (f'{var} = {answer}')
    elif Type == 'em':
        which = input(
            'Which equation (v=u+at (1) or s=ut+(1/2)at² (2) or v² = u² + 2as (3) or a = (v-u)/t (4) )? ')
        if which == '1':
            Givens = input(
                'Givens (order: v u a t. If haven\'t got then put in ?): ')
            a = give(Givens)
            t, v, u, a = a[3], a[0], a[1], a[2]
            answer = eq1(v, u, a, t)
            var, answer = answer[0], answer[1]
            return (f'{var} = {answer}')
        elif which == '2':
            Givens = input(
                'Givens (order: s u a t. If haven\'t got then put in ?): ')
            a = give(Givens)
            t, s, u, a = a[3], a[0], a[1], a[2]
            answer = eq2(s, u, a, t)
            if answer == 'no':
                return ('Retry the program with another equation to find your variable.')
            else:
                var, answer = answer[0], answer[1]
                return (f'{var} = {answer}')
        elif which == '3':
            Givens = input(
                'Givens (order: v u a s. If haven\'t got then put in ?): ')
            a = give(Givens)
            s, v, u, a = a[3], a[0], a[1], a[2]
            answer = eq3(v, u, a, s)
            if answer == 'no':
                return ('Retry the program with another equation to find your variable.')
            else:
                var, answer = answer[0], answer[1]
                return (f'{var} = {answer}')
        elif which == '4':
            Givens = input(
                'Givens (order: a v u t. If haven\'t got then put in ?): ')
            a = give(Givens)
            t, a, v, u = a[3], a[0], a[1], a[2]
            answer = eq4(a, v, u, t)
            var, answer = answer[0], answer[1]
            return (f'{var} = {answer}')
