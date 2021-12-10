# test

import random
def dice():
    """Return an random integer value"""
    return random.randint(1, 6)

def roll(num):
    """Return the list value of number of random integer"""
    return [dice() for i in range(num)]

def getDiceFace(index):
    return {1 : u"\u2680", 2 : u"\u2681", 3 : u"\u2682", 4 : u"\u2683", 5 : u"\u2684", 6 : u"\u2685"}.get(index)

def listDiceFace(lis):
    return [getDiceFace(i) for i in lis]

def printDiceRoll(diceRoll):
    print(f'Result : {", ".join(listDiceFace(diceRoll))} (It\'s {", ".join(map(str, diceRoll))})')


#110 Meter Hurdles
print("""Throw all five dice, up to 6 times, until you are satisfied with the result.
The final score will be the total value of all five dice of the last attempt.""")
final = 0
for i in range(6):
    rolls = roll(5)
    printDiceRoll(rolls)
    final = sum(rolls)
    user = input("Do you want to stop(please answer with yes or no)? ")
    if user.lower() == "yes":
        break
print("\nGame ended")
print(f"Final Score: {final}")

#Pole-Vault
print("\n\n")
print("""Jumping starts at the height of 10 and is increased by 2 each turn. Players take turn for each height or can decide to skip it.
You have three attempts for each height. Throw two to eight dice to equal or exceeds the current height without any 1s.
The final socre will be the maximum height which was mastered.""")
height = 10
nexth = 2
final = 0
while True:
    print(f"Current height is {height}.")
    user = input('Would you like to have turn or skip it(please answer with "have" or "skip")?')
    if user.lower() == "skip":
        height += nexth
        continue
    for i in range(3):
        result = 0
        rolls = []
        diceroll = 0
        while True:
            user = input("How many dice do you want to roll from two to eight dice?")
            try:
                diceroll = int(user)
                if not diceroll <=  1 or diceroll >= 9:
                    break
                print("Invalid Move")
            except ValueError:
                print("Invalid Move")
        rolls = roll(diceroll)
        result = sum(rolls)
        TF = False
        printDiceRoll(rolls)
        if 1 in rolls:
            TF = True
            print("Dice roll has 1 included.")
        if result < height or TF:
            print("Faild.\nPlease retry!!")
            continue
        print(f"Passed the height {height}")
        final = height
        break
    if not final == height:
        break
    height += nexth
print("\nGame Ended")
print(f"Final Score : {final}")
