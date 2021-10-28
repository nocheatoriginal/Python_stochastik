# Copyright 2021 - Nils Pourié
#
#
import os
# P(X = k) = p^k * (1- p)^n-k * n über k
def bernouliFormel(p, n, k):
    return potenz(p, k) * potenz((1-p), n-k) * binomialkoeffizient(n, k)

# Binomialkoeffizient: n, k >> n! / k! * (n-k)!
def binomialkoeffizient(n, k):
    try:
        if k == 0:
            return int(fakultät(n) / (fakultät(k) * fakultät(n-k))) # Immer 1 da: ergebnis = n / (1 * (n - 0) = n / n = 1
        elif k > n or k < 0 or n < 0:
            # print("FEHLER: k > n")
            return 0
        else:
            return fakultät(n) / (fakultät(k) * fakultät(n-k))
    except:
            print("FEHLER")
            return 0 # oder Null ..., aber Null sorgt immer für bernouliFormel(...) = 0.0

# Fakultät x! = (x+1)! / (x+1)
def fakultät(zahl):
    ergebnis = zahl
    if zahl < 0:
        print("FEHLER")
        return 0 # "FEHLER"
    elif zahl == 0: 
        return int(fakultät(zahl + 1)/(zahl + 1)) # 0! = 1! / 1
    else:
        while zahl > 1:
            ergebnis *= (zahl -1)
            zahl -= 1
    return ergebnis
    #else:
    #    while zahl < -1:
    #        ergebnis *= (zahl +1)
    #        zahl +=1
    #    ergebnis = 0

def potenz(basis, exponent):
    if exponent == 0:
        ergebnis = 1
    elif exponent < 0:
        positivexponent = exponent * (-1)
        ergebnis = basis
        for i in range(positivexponent -1):
            ergebnis *= basis
        ergebnis = 1/ergebnis
    else:
        ergebnis = basis
        for i in range(exponent -1):
            ergebnis *= basis
    return ergebnis

# Alternativer Algorithmus
def altPotenz(zahl, hoch):
    if hoch < 0:
        neg = True
        hoch *= hoch
    else:
        neg = False
    ergebnis = (hoch-1) * (zahl * zahl)
    if hoch == 0:
        ergebnis = 1
    elif hoch == 1:
        ergebnis = zahl
    if neg:
        ergebnis = 1/ergebnis
    return ergebnis

def binomCdf(n, p, untereGrenze, obereGrenze):
    ergebnis = 0
    while True:
        if untereGrenze > obereGrenze:
            break
        ergebnis += bernouliFormel(p, n, untereGrenze)
        untereGrenze += 1
    return ergebnis

def dezimalzahl(zähler, nenner):
    return zähler/nenner


def beispiele():
    print("Beispiel (binomCdf(8, 1/3, 5, 8)):")
    print(binomCdf(8, 1/3, 5, 8))
    print(">>>")
    print("Beispiel (bernouliFormel(1/3, 8, 5)):")
    print(bernouliFormel(1/3, 8, 5))
    print(">>>")
    print("Beispiel (binomialkoeffizient(12, 5)):")
    print(binomialkoeffizient(12, 5))
    print(">>>")
    print("Beispiel (fakultät(6)):")
    print(fakultät(6))
    print(">>>")
    print("Beispiel potenz(3, 0):")
    print(potenz(3,0))
    print(">>>")
    print("Beispiel altPotenz(3, 0):")
    print(altPotenz(3,0))
    print(">>>")
    print("Beispiel potenz(2, -1):")
    print(potenz(2,-1))
    print(">>>")
    print("Beispiel altPotenz(2, -1):")
    print(altPotenz(2,-1))

    print(f"Test: {binomCdf(3, 1/4, 0, 3) = }")
    print(f"{bernouliFormel(1/4, 3, 0) = }")
    print(f"{bernouliFormel(1/4, 3, 1) = }")
    print(f"{bernouliFormel(1/4, 3, 2) = }")
    print(f"{bernouliFormel(1/4, 3, 3) = }")
    print("---------------------------------------")
    print("Copyright 2021 - Nils Pourié\n")



# TODO Auswahlmenu
def menu():
    print("Menu\n----")
    print("[1] fakultät(zahl)")
    print("[2] potenz(basis, exponent)")
    print("[3] binomialkoeffizient(n, k)")
    print("[4] bernouliFormel(p, n, k)")
    print("[5] binomCdf(n, p, untereGrenze, obereGrenze)")
    print("[6] dezimalzahl(zähler, nenner)")
    print("clear")
    print("exit")
    print("----")

def main():
    running = True
    beispiele()

    while running:
        menu()
        _eingabe = input("Eingabe > ")
        print()

        if _eingabe == "1":
            print("[1] fakultät(zahl)")
            parameter1 = input("Parameter eingeben >>> ")
            print(f"{fakultät(int(parameter1))}")
            print()
        elif _eingabe == "2":
            print("[2] potenz(basis, exponent)")
            parameter2 = input("Parameter eingeben >>> ")
            print(f'{potenz(int(parameter2.split(", ")[0]), int(parameter2.split(", ")[1]))}')
            print()
        elif _eingabe == "3":
            print("[3] binomialkoeffizient(n, k)")
            parameter3 = input("Parameter eingeben >>> ")
            print(f'{binomialkoeffizient(int(parameter3.split(", ")[0]), int(parameter3.split(", ")[1]))}')
            print()
        elif _eingabe == "4":
            print("[4] bernouliFormel(p, n, k)")
            parameter4 = input("Parameter eingeben >>> ")
            print(f'{bernouliFormel(float(parameter4.split(", ")[0]), int(parameter4.split(", ")[1]), int(parameter4.split(", ")[2]))}')
            print()
        elif _eingabe == "5":
            print("[5] binomCdf(n, p, untereGrenze, obereGrenze)")
            parameter5 = input("Parameter eingeben >>> ")
            print(f'{binomCdf(int(parameter5.split(", ")[0]), float(parameter5.split(", ")[1]), int(parameter5.split(", ")[2]), int(parameter5.split(", ")[3])) = }')
            # Als Bruch, allerdings keine Dezimalzahl mehr möglich...   print(f'{binomCdf(int(parameter5.split(", ")[0]), int(parameter5.split(", ")[1].split("/")[0])/int(parameter5.split(", ")[1].split("/")[1]), int(parameter5.split(", ")[2]), int(parameter5.split(", ")[3])) = }')
            print()
        elif _eingabe == "6":
            print("[6] dezimalzahl(zähler, nenner)")
            parameter6 = input("Parameter eingeben >>> ")
            print(f'{dezimalzahl(int(parameter6.split("/")[0]), int(parameter6.split("/")[1]))}')
            print()
        elif _eingabe == "clear":
            # Sofern Programm auf Windows-Rechner läuft:
            clear = lambda: os.system('cls')
            clear()
        elif _eingabe == "exit":
            print("Verlassen")
            running = False
        else:
            print(f"'{_eingabe}': command not found")

    print("Vielen Dank für die Benutzung!")

if __name__ == '__main__':
    main()
