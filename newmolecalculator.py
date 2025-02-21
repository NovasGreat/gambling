from numpy import random
import time
import os
import math
import numpy as np
import platform

# this took me so damn long holy

mol = 6.02e23
molar_volume = 22.4

def os_check():
    if platform.system() == "Windows":
        os.system('cls')
    if platform.system() == "Linux":
        os.system('clear')
    if platform.system() == "Darwin":
        os.system("clear && printf '\e[3J'")
        os.system('clear')   

recent1 = 'none'
recent2 = ''
recent3 = ''
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

while True:
    try:
        os_check()
        section_1 = 1
        section_2 = 1
        section_3 = 1
        section_4 = 1
        print('Mole Calculation (One-Step and Two-Step)')
        print('')
        print(f'Most Recent Equation: {recent1}')
        print(f'{recent2}')
        print(f'{recent3}')
        print('')
        input('Push Enter to start! ')
        given = input('What did the problem give you? (liters, grams, molecules, moles): ')
        wants = input('What does the problem want? (liters, grams, molecules, moles): ')
        str_given = given
        str_wants = wants
        os_check()
        if given == wants:
            time.sleep(2)
            print("You can't do that...")
            time.sleep(2)
            input('(Enter to continue...) ')
            continue

        if given == 'molecules':
           given_molecules = input('What is the molecule amount?: ')
           given = given_molecules
           section_2 = 6.02e23
   
        if str_given == 'liters':
           given_liters = input('What is the liters amount?: ') 
           given = given_liters
           section_2 = 22.4
     
        if given == 'moles':
            given_moles = input('What is the moles amount?: ')
            given = given_moles
            section_2 = 1
        if str_given == 'grams':
            given_grams = input('What is the grams amount?: ')
            given = given_grams
        if str_given == 'grams' or str_wants == 'grams':
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
            given_molar_mass = (float(mass1)*float(amount1)) + (float(mass2)*float(amount2)) + (float(mass3)*float(amount3)) + (float(mass4)*float(amount4)) + (float(mass5)*float(amount5))
        if str_given == 'grams':
            section_2 = given_molar_mass
        if str_wants == 'grams' and str_given == 'moles':
            section_1 = given_molar_mass
        if str_given != 'moles' and str_given != 'moles':  
            if wants == 'molecules':
                section_3 = 6.02e23
                section_4 = 1
            if wants == 'grams':
                section_3 = given_molar_mass
                section_4 = 1
            if wants == 'liters':
                section_3 = 22.4
                section_4 = 1

        if str_wants == 'liters' and str_given == 'moles':
            section_1 = 22.4
        if str_wants == 'molecules' and str_given == 'moles':
            section_1 = 6.02e23

        
        
        
        time.sleep(1)
        os_check()
        
        total = float(given) * (float(section_1)/float(section_2)) * (float(section_3)/float(section_4))
        rounded = format(total,'.4g')
        print(f'The equation used: {total} = {given} * ({section_1} / {section_2}) * ({section_3} / {section_4})')
        
        recent1 = (f'{total} = {given} * ({section_1} / {section_2}) * ({section_3} / {section_4})')
        recent2 = (f'There are {total} {str_wants} in {given} {str_given}.')
        recent3 = (f'Rounded (by 2nd decimal): {rounded}')
        print('')
        print(f'There are {total} {str_wants} in {given} {str_given}.')
        print(f'Rounded (by 2nd decimal): {rounded}')
        input('Enter to continue...')
    except ValueError:
        error