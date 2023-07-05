# Heads and Tails stimulator

import random  # Random makes it easy to choose in these situations

print('.\n \tWelcome to the "Heads & Tails Cricket Game"\n')  # Greetings


choices = [["heads", "head"], ["tails", "tail"]]  # Some people forget the 's' offtenly
choice_player = input("\tSelect 'Heads' or 'Tails':\n\t\t").lower()
toss = random.choice(choices)

if choice_player in choices[0] or choice_player in choices[1]:
    if choice_player in toss:
        print("You have won!!!")
    else:
        print("You lost!!!")
else:
    print("Please input either 'Heads' or 'Tails'")
