from cmath import pi
from shutil import which
import time
import math
from scipy.constants import gravitational_constant as gc
import numpy as np


def wrong():
    time.sleep(0.5)
    print("\nRetry\n")
    time.sleep(0.5)


def conv1(input1, range1):
    try:
        input1 = int(input1)
        if input1 not in range1:
            wrong()
            return False
        else:
            return input1
    except ValueError:
        wrong()
        return False


def which_unknown(num):
    try:
        num = float(num)
        return num, 0, False
    except ValueError:
        if num != "?":
            return num, 10, False
        else:
            return num, 1, True


def tot_check_if(tot_check):
    if tot_check >= 10:
        print("Something entered was incorrect")
        return False
    elif tot_check in range(2, 4):
        print("Too many unknown variables entered")
        return False
    elif tot_check == 0:
        print("No variable to be found in equation")
        return False
    else:
        return True


def tot_check_3(v1, v2, v3):
    return v1[1] + v2[1] + v3[1]


def tot_check_4(v1, v2, v3, v4):
    return v1[1] + v2[1] + v3[1] + v4[1]


eq1 = "v = 2πrf"
eq2 = "a꜀ = v²/r"
eq3 = "Fₙₑₜ = mv²/r"
eq4 = "F = GMm/r²"
eq5 = "g = F/m = GM/r²"
eq6 = "T²/r³ = 4π²/GM"


def equation(which):
    finished = False
    while finished == False:
        print(
            "\nFor the following enter either the value of the variable or a question mark (?):"
        )
        if which == 1:
            vel = input("Velocity: ")
            rad = input("Radius: ")
            freq = input("Frequency (or 1/Period as number not fraction): ")

            vel_check = which_unknown(vel)
            rad_check = which_unknown(rad)
            freq_check = which_unknown(freq)

            total_check = tot_check_if(tot_check_3(vel_check, rad_check, freq_check))

            if total_check == True:
                if vel_check[2] == True:
                    print(f"{eq1}")
                    print(f"v = 2π \u2A2F {rad_check[0]} \u2A2F {freq_check[0]}")
                    print(f"v = {2*pi*rad_check[0]*freq_check[0]} m/s")
                    finished = True
                elif rad_check[2] == True:
                    print("r = v/2πf")
                    print(f"r = {vel_check[0]}/2π \u2A2F {freq_check[0]}")
                    print(f"r = {vel_check[0]/(2*pi*freq_check[0])} m")
                    finished = True
                else:
                    print("f = v/2πr")
                    print(f"f = {vel_check[0]}/2π \u2A2F {rad_check[0]}")
                    print(f"f = {vel_check[0]/(2*pi*rad_check[0])} Hz")
                    finished = True
        elif which == 2:
            acc = input("Centripetal Acceleration: ")
            vel = input("Velocity: ")
            rad = input("Radius: ")

            acc_check = which_unknown(acc)
            vel_check = which_unknown(vel)
            rad_check = which_unknown(rad)

            total_check = tot_check_if(tot_check_3(acc_check, vel_check, rad_check))

            if total_check == True:
                if acc_check[2] == True:
                    print(f"{eq2}")
                    print(f"a꜀ = {vel_check[0]}\u00B2/{rad_check[0]}")
                    print(f"a꜀ = {pow(vel_check[0], 2)/rad_check[0]} m/s\u00B2")
                    finished = True
                elif vel_check[2] == True:
                    print("v = \u221Aa꜀r")
                    print(f"v = \u221A{acc_check[0]} \u2A2F {rad_check[0]}")
                    print(f"v = {math.sqrt(acc_check[0]*rad_check[0])} m/s")
                    finished = True
                else:
                    print("r = v\u00B2/a꜀")
                    print(f"r = {vel_check[0]}\u00B2/{acc_check[0]}")
                    print(f"r = {pow(vel_check[0], 2)/acc_check[0]} m")
                    finished = True
        elif which == 3:
            force = input("Net Force: ")
            mass = input("Mass: ")
            vel = input("Velocity: ")
            rad = input("Radius: ")

            force_check = which_unknown(force)
            mass_check = which_unknown(mass)
            vel_check = which_unknown(vel)
            rad_check = which_unknown(rad)

            total_check = tot_check_if(
                tot_check_4(force_check, mass_check, vel_check, rad_check)
            )

            if total_check == True:
                if force_check[2] == True:
                    print(f"{eq3}")
                    print(
                        f"Fₙₑₜ = {mass_check[0]} \u2A2F {vel_check[0]}\u00B2/{rad_check[0]}"
                    )
                    print(f"Fₙₑₜ = {mass_check[0]*pow(vel_check[0], 2)/rad_check[0]} N")
                    finished = True
                elif mass_check[2] == True:
                    print("m = Fₙₑₜr/v\u00B2")
                    print(
                        f"m = {force_check[0]} \u2A2F {rad_check[0]}/{vel_check[0]}\u00B2"
                    )
                    print(
                        f"m = {(force_check[0]*rad_check[0])/pow(vel_check[0], 2)} kg"
                    )
                    finished = True
                elif vel_check[2] == True:
                    print("v = \u221AFₙₑₜr/m")
                    print(
                        f"v = \u221A{force_check[0]} \u2A2F {rad_check[0]}/{mass_check[0]}"
                    )
                    print(
                        f"v = {math.sqrt((force_check[0]*{rad_check[0]})/{mass_check[0]})} m/s"
                    )
                    finished = True
                else:
                    print("r = v\u00B2m/Fₙₑₜ")
                    print(
                        f"r = {vel_check[0]}\u00B2 \u2A2F {mass_check[0]}/{force_check[0]}"
                    )
                    print(
                        f"r = {(pow(vel_check[0], 2)*{mass_check[0]})/force_check[0]} m"
                    )
                    finished = True
        elif which == 4:
            force = input("Force: ")
            l_mass = input("Larger Mass: ")
            s_mass = input("Smaller Mass: ")
            rad = input("Radius: ")

            force_check = which_unknown(force)
            l_check = which_unknown(l_mass)
            s_check = which_unknown(s_mass)
            rad_check = which_unknown(rad)

            total_check = tot_check_if(
                tot_check_4(force_check, l_check, s_check, rad_check)
            )

            if total_check == True:
                if force_check[2] == True:
                    print(f"{eq4}")
                    print(f"F = {gc}{l_check[0]}{s_check[0]}/{rad_check[0]}\u00B2")
                    print(f"F = {(gc*l_check[0]*s_check[0])/pow(rad_check[0], 2)} N")
                    finished = True
                elif l_check[2] == True:
                    print("M = Fr\u00B2/Gm")
                    print(
                        f"M = {force_check[0]} \u2A2F {rad_check[0]}\u00B2/{gc} \u2A2F {s_check[0]}"
                    )
                    print(
                        f"M = {(force_check[0]*pow(rad_check[0], 2))/(gc*s_check[0])} kg"
                    )
                    finished = True
                elif s_check[2] == True:
                    print("m = Fr\u00B2/GM")
                    print(
                        f"m = {force_check[0]} \u2A2F {rad_check[0]}\u00B2/{gc} \u2A2F {l_check[0]}"
                    )
                    print(
                        f"m = {(force_check[0]*pow(rad_check[0], 2))/(gc*l_check[0])} kg"
                    )
                    finished = True
                else:
                    print("r = \u221AGMm/F")
                    print(
                        f"r = \u221A{gc} \u2A2F {l_check[0]} \u2A2F {s_check[0]}/{force_check[0]}"
                    )
                    print(f"r = {math.sqrt((gc*l_check[0]*s_check[0])/force_check)} m")
                    finished = True
        elif which == 5:
            f_o_s = 0
            while f_o_s not in range(1, 3):
                f_o_s = input(
                    "Enter either 1 or 2 depending on either 'g = F/m' or 'g = GM/r²': "
                )
                conv = conv1(f_o_s, range(1, 3))
                if conv != False:
                    f_o_s = conv
            if f_o_s == 1:
                grav = input("Gravitational Constant (g): ")
                force = input("Force: ")
                mass = input("Small Mass: ")

                grav_check = which_unknown(grav)
                force_check = which_unknown(force)
                mass_check = which_unknown(mass)

                total_check = tot_check_if(
                    tot_check_3(grav_check, force_check, mass_check)
                )

                if total_check == True:
                    if grav_check[2] == True:
                        print("g = F/m")
                        print(f"g = {force_check[0]}/{mass_check[0]}")
                        print(f"g = {force_check[0]/mass_check[0]} N/kg")
                        finished = True
                    elif force_check[2] == True:
                        print("F = gm")
                        print(f"F = {grav_check[0]} \u2A2F {mass_check[0]}")
                        print(f"F = {grav_check[0]*mass_check[0]} N")
                        finished = True
                    else:
                        print("m = F/g")
                        print(f"m = {force_check[0]}/{grav_check[0]}")
                        print(f"m = {force_check[0]/grav_check[0]} kg")
                        finished = True
            else:
                grav = input("Gravitational Constant: ")
                l_mass = input("Larger Mass: ")
                rad = input("Radius: ")

                grav_check = which_unknown(grav)
                l_check = which_unknown(l_mass)
                rad_check = which_unknown(rad)

                total_check = tot_check_if(tot_check_3(grav_check, l_check, rad_check))

                if total_check == True:
                    if grav_check[2] == True:
                        print("g = GM/r²")
                        print(f"g = {gc}{l_check[0]}/{rad_check[0]}\u00B2")
                        print(f"g = {(gc*l_check[0])/pow(rad_check[0], 2)} N/kg")
                        finished = True
                    elif l_check[2] == True:
                        print("M = gr\u00B2/G")
                        print(f"M = {grav_check[0]} \u2A2F {rad_check[0]}\u00B2/{gc}")
                        print(f"M = {(force_check[0]*pow(rad_check[0], 2))/gc} kg")
                        finished = True
                    else:
                        print("r = \u221AGM/g")
                        print(f"r = \u221A{gc} \u2A2F {l_check[0]}/{grav_check[0]}")
                        print(f"r = {math.sqrt((gc*l_check[0])/grav_check)} m")
                        finished = True
        else:
            # 'T²/r³ = 4π²/GM'
            period = input("Period: ")
            radius = input("Radius: ")
            l_mass = input("Larger Mass: ")

            period_check = which_unknown(period)
            rad_check = which_unknown(radius)
            l_check = which_unknown(l_mass)

            total_check = tot_check_if(tot_check_3(period_check, rad_check, l_check))

            if total_check == True:
                if period_check[2] == True:
                    print("T = \u221A4π²r³/GM")
                    print(f"T = \u221A4π² \u2A2F {rad_check[0]}³/{gc}{l_check[0]}")
                    print(
                        f"T = {math.sqrt((4*pow(pi, 2)*pow(rad_check[0], 3))/(gc*l_check[0]))} s"
                    )
                    finished = True
                elif rad_check[2] == True:
                    print("r = \u221BT²GM/4π²")
                    print(
                        f"r = \u221B{period_check[0]}² \u2A2F {gc} \u2A2F {l_check[0]}/4π²"
                    )
                    print(
                        f"r = {np.cbrt((pow(period_check[0], 2)*gc*l_check[0])/(4*pow(pi, 2)))} m"
                    )
                    finished = True
                else:
                    print("M = 4π²r³/GT²")
                    print(
                        f"M = 4π² \u2A2F {rad_check[0]}³/{gc} \u2A2F {period_check[0]}²"
                    )
                    print(
                        f"M = {(4*pow(pi, 2)*pow(rad_check[0], 3))/(gc*pow(period_check[0], 2))} m"
                    )
                    finished = True


def main():
    which_eq = 0
    rng = range(1, 7)

    while which_eq not in rng:
        print("To choose an equation enter listed number:")
        which_eq = input(
            f"1: {eq1}\n2: {eq2}\n3: {eq3}\n4: {eq4}\n5: {eq5}\n6: {eq6}\nChoice: "
        )
        conv = conv1(which_eq, rng)
        if conv != False:
            which_eq = conv

    equation(which_eq)
