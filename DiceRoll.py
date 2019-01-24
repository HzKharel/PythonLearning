import  random

playAgain = True

def random_dice():
    x = random.randint(1,6)
    return x

while playAgain:
    y = random_dice()
    print("You rolled:", y)
    if input("Would you like to roll again!?") == "no":
        break
