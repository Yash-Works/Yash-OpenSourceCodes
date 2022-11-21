# Rock Paper Scissor
import random
print("Welcome to the RPS game")
uc = input("Enter a Choice: ")
ci = ("Rock","Paper","Scissors")
cc = random.choice(ci)
print("Opponent: ",cc)
if uc == cc:
    print("Draw")
elif uc == "Rock":
    if cc == "Scissors":
        print("You Won")
    else:
        print("You Lose")
elif uc == "Paper":
    if cc == "Rock":
        print("You Won")
    else:
        print("You Lose")
elif uc == "Scissors":
    if cc == "Paper":
        print("You Won")
    else:
        print("You Lose")