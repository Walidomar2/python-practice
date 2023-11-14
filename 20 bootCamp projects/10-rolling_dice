
########################################################################################
#Author: Walid Omar
#Brief:This Python script simulates rolling two six-sided dice and displays the results
#with corresponding ASCII art representations of the dice faces. Users can choose
#to roll the dice or exit the program.
########################################################################################

import random


DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

def rollingDice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    print(f"dice1 rolled: {dice1} ")
    print("\n".join(DICE_ART[dice1]))
    
    print(f"dice2 rolled: {dice2} ")
    print("\n".join(DICE_ART[dice2]))
    
while True:
    answer = input("Roll the dice? (Y/N): ").strip().capitalize()
    
    if answer == 'Y':
        rollingDice()
    else:
        break
    

 