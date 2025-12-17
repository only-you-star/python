import random

def game():
    computer = random.choice([0, -1, 1])
    G = input("Enter your choice (r for Rock, p for Paper, s for Scissor) :  ")
    userdict = {"r": 0, "p": 1, "s": -1}
    computerdict = {0: "rock", 1: "paper", -1: "scissor"}
    
    if G not in userdict:
        print("Invalid choice! Please enter r, p, or s.")
        return game()
    
    yourechoice = userdict[G]
    print(f"You chose {computerdict[yourechoice]} and computer chose {computerdict[computer]}")
    
    if computer == yourechoice:
        print("It's a draw!")
    else:
        if computer - yourechoice == 1 or computer - yourechoice == -2:
            print("You lose!")
        else:
            print("You win!")

game()