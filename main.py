from numpy import random
import time
import os
import math
import numpy as np

cd = .5
times = 0
amount = 1



#----------------------
main = [
'Dirt - 1/2'
, "Oak Log - 1/4"
, "1/8"
, "Leaves - 1/16"
, "1/32" 
, "Diamond - 1/64"
]
probability = [.50, .25, .125, .0625, .03125, .03125]
probability = np.array(probability)
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

eight = np.array([
"Cobblestone - 1/8",
"Wool - 1/8"
])




while True:
    try:
        os.system('clear')
        print("Fake RNG")
        print ('1 - gamble')
        print ('2 - exit')
        print ('')
        print('times gambled: '+str(times))
        aa = sum(probability)
        print(aa)
        choice = input('what u want to do: ')
        
        if int(choice) == 1:
            roll = np.random.choice(main,p=probability, replace=True,size=amount)
            
            if roll == "1/32":
                roll = np.random.choice(thirtytwo, replace=True,size=amount)
            times = times + amount
            print(str(roll))
            time.sleep(cd)
            continue
        
        if int(choice) == 2:
            print('bai')
            break
        else:
            continue
        break
    except ValueError:
        error
    
        