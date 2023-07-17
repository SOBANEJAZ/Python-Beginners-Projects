"""MOTIVATION GIVER PROGRAM TO BOOST YOUR MOTIVATION TO DO HARD STUFF"""

from random import choice as motive  # importing choice as motive
m1 = "Never give up"  # Some of the motivation quotes
m2 = "You are the Best and no one can defeat you"
m3 = "No pain No Gain"
m4 = "Hardwork pays off"
m5 = "Success is not the destination but it is a journey"
m6 = "Journey of a thousand miles start with a single step"
m7 = "If you Give you on your Goals you give up on life"
m8 = "honesty is the best policy"
m9 = "The one who never gives up is the one who always wins the game of life"
m10 = "When your privileges become desires then you have nothing in life"

m_all = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]  #all the quotes are listed in this list


approve = input("Do you want motivation: (Y/N)").lower()  #This startes the program
while True:
    if approve == "y":
        motivation = motive(m_all)
        print(f"\n {motivation}")
        approve2 = input("Do you want more motivation: (Y/N)").lower()
        if approve2 == "n":
            break
    else:
        print("Then go and ruin your life and close the program")
        break

#suiiii