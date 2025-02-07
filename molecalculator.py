from numpy import random
import time
import os
import math
import numpy as np
import platform

mol = 6.02e23
molar_volume = 22.4


 

def results():
    os_check()
    print('Getting Results...')
    time.sleep(1)
    os_check()
    

def ph():
    print("placeholder")
    
def os_check():
    if platform.system() == "Windows":
        os.system('cls')
    if platform.system() == "Linux":
        os.system('clear')
    if platform.system() == "Darwin":
        os.system("clear && printf '\e[3J'")
        os.system('clear')   

atomic_masses = {
    "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81, "C": 12.011,
    "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180, "Na": 22.990, "Mg": 24.305,
    "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06, "Cl": 35.45, "Ar": 39.948,
    "K": 39.098, "Ca": 40.078, "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996,
    "Mn": 54.938, "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38,
    "Ga": 69.723, "Ge": 72.63, "As": 74.922, "Se": 78.971, "Br": 79.904, "Kr": 83.798,
    "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224, "Nb": 92.906, "Mo": 95.95,
    "Tc": 98, "Ru": 101.07, "Rh": 102.91, "Pd": 106.42, "Ag": 107.87, "Cd": 112.41,
    "In": 114.82, "Sn": 118.71, "Sb": 121.76, "Te": 127.60, "I": 126.90, "Xe": 131.29,
    "Cs": 132.91, "Ba": 137.33, "La": 138.91, "Ce": 140.12, "Pr": 140.91, "Nd": 144.24,
    "Pm": 145, "Sm": 150.36, "Eu": 151.96, "Gd": 157.25, "Tb": 158.93, "Dy": 162.50,
    "Ho": 164.93, "Er": 167.26, "Tm": 168.93, "Yb": 173.05, "Lu": 174.97, "Hf": 178.49,
    "Ta": 180.95, "W": 183.84, "Re": 186.21, "Os": 190.23, "Ir": 192.22, "Pt": 195.08,
    "Au": 196.97, "Hg": 200.59, "Tl": 204.38, "Pb": 207.2, "Bi": 208.98, "Po": 209,
    "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232.04, "Pa": 231.04,
    "U": 238.03, "Np": 237, "Pu": 244, "Am": 243, "Cm": 247, "Bk": 247, "Cf": 251,
    "Es": 252, "Fm": 257, "Md": 258, "No": 259, "Lr": 262, "Rf": 267, "Db": 270,
    "Sg": 271, "Bh": 270, "Hs": 277, "Mt": 278, "Ds": 281, "Rg": 282, "Cn": 285,
    "Nh": 286, "Fl": 289, "Mc": 290, "Lv": 293, "Ts": 294, "Og": 294, "stop":"stop"
}

print('Loading...')
time.sleep(2)
os_check()
while True:
    try:
        os_check()
        print('Moles Calculations')
        print('')
        print('Moles Calculator - 1')
        print('Moles Conversion - 2')
        print('')
        user_input = input("Where do you want to go?: ")

        if int(user_input) == 1:
            os_check()
            print('Moles Calculator')
            print('')
            print('How many atoms will you be adding?')
            print('Minimum is one, maximum is five, input the number!')
            print('')
            user_input = input('Enter here: ')
            if int(user_input) == 1:
                element1 = input("Enter the first element symbol: ")  # Example: "C"
                amount1 = input(f'How many atoms of {element1} are there?: ')
                mass1 = atomic_masses.get(element1, "NaN")
                user_input = input('Do you want it rounded to the whole number? (Yes or No): ')
                if str(user_input) == "Yes":
                    total = int(mass1) * int(amount1)
                if str(user_input) == "No":
                    total = float(mass1) * float(amount1)
                else:
                    continue
                results()
                print(f"The total mass is {total} g/mol.")
                input('(Enter to continue...).')
                continue
            if int(user_input) == 2:
                element1 = input("Enter the first element symbol: ")  # Example: "C"
                amount1 = input(f'How many atoms of {element1} are there?: ')
                element2 = input("Enter the second element symbol: ")  # Example: "C"
                amount2 = input(f'How many atoms of {element2} are there?: ')
                mass1 = atomic_masses.get(element1, "NaN")
                mass2 = atomic_masses.get(element2, "NaN")
                user_input = input('Do you want it rounded to the whole number? (Yes or No): ')
                if str(user_input) == "Yes":
                    total = int(mass1)*int(amount1) + int(mass2)*int(amount2)
                if str(user_input) == "No":
                    total = float(mass1)*float(amount1) + float(mass2)*float(amount2)
                else:
                    continue
                print(f"The mass is {total} g/mol.")
                input('(Enter to continue...).')
                continue
            if int(user_input) == 3:
                element1 = input("Enter the first element symbol: ")  # Example: "C"
                amount1 = input(f'How many atoms of {element1} are there?: ')
                element2 = input("Enter the second element symbol: ")  # Example: "C"
                amount2 = input(f'How many atoms of {element2} are there?: ')
                element3 = input("Enter the third element symbol: ")  # Example: "C"
                amount3 = input(f'How many atoms of {element3} are there?: ')
                mass1 = atomic_masses.get(element1, "NaN")
                mass2 = atomic_masses.get(element2, "NaN")
                mass3 = atomic_masses.get(element3, "NaN")
                user_input = input('Do you want it rounded to the whole number? (Yes or No): ')
                if str(user_input) == "Yes":
                    total = int(mass1)*int(amount1) + int(mass2)*int(amount2) + int(mass3)*int(amount3)
                if str(user_input) == "No":
                    total = float(mass1)*float(amount1) + float(mass2)*float(amount2) + float(mass3)*float(amount3)
                else:
                    continue
                results()
                print(f"The mass is {total} g/mol.")
                input('(Enter to continue...).')
                continue
            if int(user_input) == 4:
                element1 = input("Enter the first element symbol: ")  # Example: "C"
                amount1 = input(f'How many atoms of {element1} are there?: ')
                element2 = input("Enter the second element symbol: ")  # Example: "C"
                amount2 = input(f'How many atoms of {element2} are there?: ')
                element3 = input("Enter the third element symbol: ")  # Example: "C"
                amount3 = input(f'How many atoms of {element3} are there?: ')
                element4 = input("Enter the fourth element symbol: ")  # Example: "C"
                amount4 = input(f'How many atoms of {element4} are there?: ')
                mass1 = atomic_masses.get(element1, "NaN")
                mass2 = atomic_masses.get(element2, "NaN")
                mass3 = atomic_masses.get(element3, "NaN")
                mass4 = atomic_masses.get(element4, "NaN")
                user_input = input('Do you want it rounded to the whole number? (Yes or No): ')
                if str(user_input) == "Yes":
                    total = int(mass1)*int(amount1) + int(mass2)*int(amount2) + int(mass3)*int(amount3) + int(mass4)*int(amount4)
                if str(user_input) == "No":
                    total = float(mass1)*float(amount1) + float(mass2)*float(amount2) + float(mass3)*float(amount3) + float(mass3)*float(amount3)
                else:
                    continue
                results()
                print(f"The mass is {total} g/mol.")
                input('(Enter to continue...).')
                continue
            if int(user_input) == 5:
                element1 = input("Enter the first element symbol: ")  # Example: "C"
                amount1 = input(f'How many atoms of {element1} are there?: ')
                element2 = input("Enter the second element symbol: ")  # Example: "C"
                amount2 = input(f'How many atoms of {element2} are there?: ')
                element3 = input("Enter the third element symbol: ")  # Example: "C"
                amount3 = input(f'How many atoms of {element3} are there?: ')
                element4 = input("Enter the fourth element symbol: ")  # Example: "C"
                amount4 = input(f'How many atoms of {element4} are there?: ')
                element5 = input("Enter the fifth element symbol: ")  # Example: "C"
                amount5 = input(f'How many atoms of {element5} are there?: ')
                mass1 = atomic_masses.get(element1, "NaN")
                mass2 = atomic_masses.get(element2, "NaN")
                mass3 = atomic_masses.get(element3, "NaN")
                mass4 = atomic_masses.get(element4, "NaN")
                mass5 = atomic_masses.get(element5, "NaN")
                user_input = input('Do you want it rounded to the whole number? (Yes or No): ')
                if str(user_input) == "Yes":
                    total = int(mass1)*int(amount1) + int(mass2)*int(amount2) + int(mass3)*int(amount3) + int(mass4)*int(amount4) + int(mass5)*int(amount5)
                if str(user_input) == "No":
                    total = float(mass1)*float(amount1) + float(mass2)*float(amount2) + float(mass3)*float(amount3) + float(mass3)*float(amount3) + float(mass5)*float(amount5)
                else:
                    continue
                results()
                print(f"The mass is {total} g/mol.")
                input('(Enter to continue...).')
                continue
            else:
                os_check()
                input("Not an option! (Enter to continue...) ")
        if int(user_input) == 2:
            os_check()
            print('Moles Conversion')
            print('')
            print('Molecules and Moles Conversion - 1')
            print('Liters and Moles Conversion - 2')
            print('Grams and Moles Conversion - 3')
            print('')
            user_input = input('How do you want to convert moles? ')
            if int(user_input) == 1:
                os_check()
                user_input = input('Do you have the mole count of the chemical? (y/n): ')
                if user_input == "y":
                    mole = input('Mole amount: ')
                    os_check()
                    print('Calculating....')
                    time.sleep(1)
                    total = float(mole) * (float(mol) / float(1))
                    print(f'Amount of molecules: {total:.2e}')
                    input('Exit to continue....')
                if user_input == "n":
                    user_input = input('Do you have the molecule count of the atom? (y/n): ')
                    if user_input == 'y':
                        print('Warning: Convert the "10" into a "e" before putting in! Ex: 6.02e23 = 6.02 * 10^23')
                        molecule_amount = input('Molecule amount: ')
                        os_check()
                        print('Calculating....')
                        time.sleep(1)
                        total = float(molecule_amount) * (float(1) / float(mol))
                        print(f'Amount of moles: {total} g/mol')
                        input('Exit to continue....')

                    if user_input == 'n':
                        print("Without this information, the computer won't be able to solve this, sorry!")
                        input('Click enter to exit...')
            if int(user_input) == 2:
                os_check()
                user_input = input('Do you have the liters amount of the chemical? (y/n): ')
                if user_input == 'y':
                    mole = input('Liters count: ')
                    os_check()
                    print('Calculating....')
                    time.sleep(1)
                    total = float(mole) * (float(1) / float(molar_volume))
                    print(f'Amount of moles: {total} g/mol')
                    input('Click enter to exit...')
                if user_input == 'n':
                    user_input = input('Do you have the mole amount of the compound? (y/n): ')
                    if user_input == 'y':
                        liters = input('Mole count: ')
                        os_check()
                        print('Calculating....')
                        time.sleep(1)
                        total = float(liters) * (float(molar_volume) / float(1))
                        print(f'Volume: {total}L')
                        input('Click enter to exit...')
                    if user_input == 'n':
                        print("Without this information, the computer won't be able to solve this, sorry!")
                        input('Click enter to exit...')
            if int(user_input) == 3:
                os_check()
                user_input = input('Do you have the mole amount of the compound? (y/n): ')
                if user_input == 'y':
                    mole = input('Mole Amount: ')
                    os_check()
                    mass1 = 0
                    mass2 = 0
                    mass3 = 0
                    mass4 = 0
                    mass5 = 0
                    amount1 = 1
                    amount2 = 1
                    amount3 = 1
                    amount4 = 1
                    amount5 = 1
                    print('When you are done inputting letters, type "stop" with no spaces, then enter.')
                    element1 = input("Enter the first element symbol: ")  # Example: "C"\
                    mass1 = atomic_masses.get(element1, "NaN")
                    if mass1 == 'stop':
                        print("Ready!")
                        mass1 = 0
                    else:    
                        amount1 = input(f'How many atoms of {element1} are there?: ')
                        element2 = input("Enter the second element symbol: ")  # Example: "C"
                        mass2 = atomic_masses.get(element2, "NaN")
                        if mass2 == 'stop':
                            print("Ready!")
                            mass2 = 0
                        else:
                            amount2 = input(f'How many atoms of {element2} are there?: ')
                            element3 = input("Enter the third element symbol: ")  # Example: "C"
                            mass3 = atomic_masses.get(element3, "NaN")
                            if mass3 == 'stop':
                                print('Ready!')
                                mass3 = 0
                            else:
                                amount3 = input(f'How many atoms of {element3} are there?: ')
                                element4 = input("Enter the fourth element symbol: ")  # Example: "C"
                                mass4 = atomic_masses.get(element4, "NaN")
                                if mass4 == 'stop':
                                    print('Ready!')
                                    mass4 = 0
                                else:
                                    amount4 = input(f'How many atoms of {element4} are there?: ')
                                    element5 = input("Enter the fifth element symbol: ")  # Example: "C"
                                    mass5 = atomic_masses.get(element5, "NaN")
                                    if mass5 == 'stop':
                                        print('Ready!')
                                        mass5 = 0
                                    else:
                                        amount5 = input(f'How many atoms of {element5} are there?: ')
                    os_check()
                    print('Calculating....')
                    time.sleep(1)
                    total = float(mole) * (float(mass1)*float(amount1) + float(mass2)*float(amount2) + float(mass3)*float(amount3) + float(mass4)*float(amount4) + float(mass5)*float(amount5)) 
                    print(f"Grams: {total}")
                    input('Click Enter to continue...')
                if user_input == 'n':
                    user_input = input('Do you have the grams amount for the compound? (y/n): ')
                    if user_input == 'y':
                        grams = input('Grams: ')
                        os_check()
                        mass1 = 0
                        mass2 = 0
                        mass3 = 0
                        mass4 = 0
                        mass5 = 0
                        amount1 = 1
                        amount2 = 1
                        amount3 = 1
                        amount4 = 1
                        amount5 = 1
                        print('When you are done inputting letters, type "stop" with no spaces, then enter.')
                        element1 = input("Enter the first element symbol: ")  # Example: "C"\
                        mass1 = atomic_masses.get(element1, "NaN")
                        if mass1 == 'stop':
                            print("Ready!")
                            mass1 = 0
                        else:    
                            amount1 = input(f'How many atoms of {element1} are there?: ')
                            element2 = input("Enter the second element symbol: ")  # Example: "C"
                            mass2 = atomic_masses.get(element2, "NaN")
                            if mass2 == 'stop':
                                print("Ready!")
                                mass2 = 0
                            else:
                                amount2 = input(f'How many atoms of {element2} are there?: ')
                                element3 = input("Enter the third element symbol: ")  # Example: "C"
                                mass3 = atomic_masses.get(element3, "NaN")
                                if mass3 == 'stop':
                                    print('Ready!')
                                    mass3 = 0
                                else:
                                    amount3 = input(f'How many atoms of {element3} are there?: ')
                                    element4 = input("Enter the fourth element symbol: ")  # Example: "C"
                                    mass4 = atomic_masses.get(element4, "NaN")
                                    if mass4 == 'stop':
                                        print('Ready!')
                                        mass4 = 0
                                    else:
                                        amount4 = input(f'How many atoms of {element4} are there?: ')
                                        element5 = input("Enter the fifth element symbol: ")  # Example: "C"
                                        mass5 = atomic_masses.get(element5, "NaN")
                                        if mass5 == 'stop':
                                            print('Ready!')
                                            mass5 = 0
                                        else:
                                            amount5 = input(f'How many atoms of {element5} are there?: ')
                        os_check()
                        print('Calculating....')
                        time.sleep(1)
                        total = (float(grams) / (float(mass1)*float(amount1) + float(mass2)*float(amount2) + float(mass3)*float(amount3) + float(mass4)*float(amount4) + float(mass5)*float(amount5))) 
                        print(f"Moles: {total}")
                        input('Click Enter to continue...')
                    else:
                        print("Without this information, the computer won't be able to solve this, sorry!")
                        input('Click enter to exit...')
                
    except ValueError:
        print('error')
        continue
