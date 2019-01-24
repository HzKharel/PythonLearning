import random

userScore = 0
computerScore = 0
playGame = True

def game():
    elements = "rock", "paper", "scissors"
    userInput = ""
    global  userScore
    global  computerScore

    while userInput not in elements:
        print("Please Pick one:", elements , "Or exit to finish!")
        userInput = input()
        if userInput == "exit":
            exit()

    randomPick = random.randint(0,2)

    if elements[randomPick] == userInput:
        print("Draw!\n", "Your score:", userScore, "Computer Score:", computerScore)
    if randomPick == 0 and userInput == elements[2]:
        computerScore = computerScore + 1
        print("Computer Wins!\n", "Your score:", userScore, "Computer Score:", computerScore)
    if randomPick ==  0 and userInput == elements[1]:
        userScore = userScore + 1
        print("You Win!\n" , "Your score:", userScore, "Computer Score:", computerScore)
    if randomPick == 1 and userInput == elements[0]:
        computerScore = computerScore + 1
        print("Computer Wins!\n" + "Your score:", userScore, "Computer Score:", computerScore)
    if randomPick == 1 and userInput == elements[2]:
        userScore = userScore + 1
        print("You Win!\n", "Your score:", userScore, "Computer Score:", computerScore)
    if randomPick == 2 and userInput == elements[0]:
        userScore = userScore + 1
        print("You Win!\n" , "Your score:", userScore, "Computer Score:", computerScore)
    if randomPick == 2 and userInput == elements[1]:
        computerScore = computerScore + 1
        print("Computer Wins!\n" , "Your score:", userScore, "Computer Score:", computerScore)

while playGame:
    game()