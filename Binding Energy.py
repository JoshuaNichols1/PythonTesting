import math


def mass(am, mn, an):
    protons = an*1.007276470
    neutrons = (mn-an)*1.00866491588
    mass = (protons + neutrons) - am
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
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    finalmass = mass(float(am), float(mn), float(an))
    protonm, neutronm, finalmass = finalmass[0]
    = finalmass[1]
    = finalmass[2]
    neutron = int(mn)-int(an)
    print(f'\n{mn.translate(SUP)}{an.translate(SUB)}{es} + BE -> {an} {str(1).translate(SUP)}{str(1).translate(SUB)}P + {str(neutron)} {str(1).translate(SUP)}{str(0).translate(SUB)}N\nΔm = |RHS - LHS|\nΔm = ({str(protonm)} + {str(neutronm)}) - {am}\nΔm = {str(finalmass)}')


def be(am, mn, an):
    Binding = BE(float(am), float(mn), float(an))
    massfinal = Binding[0]
    Binding = Binding[1]
    print(f'\n∴ BE = Δm x 931.5\n= {massfinal} x 931.5\n= {Binding} MeV')


def mev(am, mn, an):
    answer = pernuc(float(am), float(mn), float(an))
    Binding = answer[0]
    answer = answer[1]
    print(f'\nPer Nucleon = MeV/nuc\n= {Binding}/{mn}\n= {answer} MeV/nuc')


def main():
    type = input('Mass, Binding Energy, MeV/Nuc or all (m, be, mev, all)? ')
    variables = input(
        'Isotope (atomic mass, mass number, atomic number, Element Symbol): ')
    prev = ''
    fin = []
    ii = 0
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
    if type == 'm':
        m(am, mn, an, es)
    elif type == 'be':
        be(am, mn, an)
    elif type == 'mev':
        mev(am, mn, an)
    elif type == 'all':
        m(am, mn, an, es)
        be(am, mn, an)
        mev(am, mn, an)
    print('')


main()
