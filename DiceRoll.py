import  random

playAgain = True

def RandomDice():
    x = random.randint(1,6)
    return x

while playAgain == True:
    y = RandomDice()
    print("You rolled:", y)
    if(input("Would you like to roll again!?") == "no"):
        break
