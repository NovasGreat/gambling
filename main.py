from numpy import random
import time
import os
import math
import numpy as np
import platform

                                     # How to commit (also push) tutorial incase i forget:
                                     # 1: git commit -m "message here"
                                     # 2: git push

cd = .5
times = 0
amount = 1
os_info = platform.uname()
roll = "none"


#----------------------
main = [
'Dirt - 1/2',
"Oak Log - 1/4",
"1/8",
"1/16",
"1/32", 
"Diamond - 1/64"
]
probability = np.array([.50, .25, .125, .0625, .03125, .03125])
probability /= probability.sum()  # normalize
print(probability)
#----------------------

#----------------------
thirtytwo = np.array([
'Furnace - 1/32',
'Stonecutter - 1/32',
'Chest - 1/32',
'Hopper - 1/32',
'Anvil - 1/32',
'Barrel - 1/32'
])

sixteen = np.array([
"Copper - 1/16",
"Iron - 1/16",
"Gold - 1/16"

])
eight = np.array([
"Cobblestone - 1/8",
"Wool - 1/8",
"Snow - 1/8",
"Lapiz Lazuli - 1/8",
"Quartz - 1/8",
"Coal - 1/8",

])




while True:
    try:
        if platform.system() == "Windows":
            os.system('cls')
        elif platform.system() == "Linux":
            os.system('clear')
        elif platform.system() == "Darwin":
            os.system("clear && printf '\e[3J'")
            os.system('clear')
        else:
            print('what os are u using bruh')
        print("Fake RNG")
        print ('1 - gamble')
        print ('0 - exit')
        print ('19 - save progress')
        print ('1567 - erase save')
        print('')
        print('times gambled: '+str(times))
        aa = sum(probability)
        print("Probability (should equal to 1 or 1.0): "+str(aa))
        print('Most Recent Roll: '+str(roll))
        choice = input('what u want to do: ')
        
        if int(choice) == 1:
            roll = np.random.choice(main,p=probability, replace=True,size=amount)
            if roll == "1/8":
                roll = np.random.choice(eight, replace=True,size=amount)
            elif roll == "1/16":
                roll = np.random.choice(sixteen, replace=True,size=amount)
            elif roll == "1/32":
                roll = np.random.choice(thirtytwo, replace=True,size=amount)
            times = times + amount
            print(str(roll))
            time.sleep(cd)
            continue
        
        if int(choice) == 0:
            print('bai')
            break
        if int(choice) == 19:
            print('placeholder')
            continue
        if int(choice) == 1567:
            print('placeholder')
            continue
        else:
            continue
        break
    except ValueError:
        continue
        