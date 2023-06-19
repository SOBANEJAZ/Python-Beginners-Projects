#  dice roller in python 

import random

# ● ┌ ─ ┐ │ └ ┘

# "┌─────────────┐"       # this is a basic example of dice
# "│             │"
# "│             │"
# "│             │"
# "│             │"
# "└─────────────┘"


dice_design = {  # these are the designs names
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = [] # the dice list that will be appended soon
total_dice = 0      #total number
num_dice = int(input(" How many dices to roll: \n \t"))     # it inputs the number of dices the user wants to roll

for i in range(num_dice): # This loops gives random numbers for dices
    dice.append(random.randint(1,6))

for i in range(num_dice):   # this loop prints the dice designs for each dice
    for j in dice_design.get(dice[i]): # this nested loop gets the design from the above list 
        print(j) # this prints the dices


for i in dice: # this loop counts the total numbers in the dices
    total_dice += i 
print(f"the total number is : {total_dice}")

# lets goooooooooo