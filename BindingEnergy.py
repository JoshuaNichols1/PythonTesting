import math


def mass(am, mn, an):
    protons, neutrons, mass = an*1.007276470, (mn-an)*1.00866491588, (protons + neutrons) - am
    if mass * -1 > mass:
        mass = mass*-1
        return str(protons), str(neutrons), str(mass)
    elif mass * -1 < mass:
        return str(protons), str(neutrons), str(mass)


def BE(am, mn, an):
    massfinal = mass(float(am), float(mn), float(an))
    massfinal = massfinal[2]
    return massfinal, (float(massfinal)*float(931.5))


def pernuc(am, mn, an):
    Binding = BE(float(am), float(mn), float(an))
    Binding = Binding[1]
    return Binding, (Binding/mn)


def m(am, mn, an, es):
    SUB, SUP = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉"), str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    finalmass = mass(float(am), float(mn), float(an))
    protonm, neutronm, finalmass, neutron = finalmass[0], finalmass[1], finalmass[2], int(mn)-int(an)
    print(f'\n{mn.translate(SUP)}{an.translate(SUB)}{es} + BE -> {an} {str(1).translate(SUP)}{str(1).translate(SUB)}P + {str(neutron)} {str(1).translate(SUP)}{str(0).translate(SUB)}N\nΔm = |RHS - LHS|\nΔm = ({str(protonm)} + {str(neutronm)}) - {am}\nΔm = {str(finalmass)}')


def be(am, mn, an):
    Binding = BE(float(am), float(mn), float(an))
    massfinal, Binding = Binding[0], Binding[1]
    print(f'\n∴ BE = Δm x 931.5\n= {massfinal} x 931.5\n= {Binding} MeV')


def mev(am, mn, an):
    answer = pernuc(float(am), float(mn), float(an))
    Binding, answer = answer[0], answer[1]
    print(f'\nPer Nucleon = MeV/nuc\n= {Binding}/{mn}\n= {answer} MeV/nuc')


def main(Type):
    Type = input('Mass, Binding Energy, MeV/Nuc or all (m, be, mev, all)? ')
    variables = input(
        'Isotope (atomic mass, mass number, atomic number, Element Symbol): ')
    prev, fin, ii = '', [], 0
    for i in variables:
        ii += 1
        if i == ' ':
            fin.append(prev)
            prev = ''
        elif ii == len(variables):
            prev += i
            fin.append(prev)
        else:
            prev += i
    am, mn, an, es = fin[0], fin[1], fin[2], fin[3]
    if Type == 'm':
        m(am, mn, an, es)
    elif Type == 'be':
        be(am, mn, an)
    elif Type == 'mev':
        mev(am, mn, an)
    elif Type == 'all':
        m(am, mn, an, es)
        be(am, mn, an)
        mev(am, mn, an)
    print('')


main()
