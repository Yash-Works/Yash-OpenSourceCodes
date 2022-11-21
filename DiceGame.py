import random

a="Yes"
min = 1
max = 6
roll_again = "Yes"
yscore = 0
oscore = 0
print("Welcome To The Game")
while a=="Yes":
    num = int(input("Enter A Number(Only 1 to 6):-"))
    ran = random.randint(min,max)
    if 1<= num<=6:
        print("Dice Is Rolling ")
        print("The Generated Number is:-", ran)
        if num == ran:
            print("You Won")
            print("Your Score:-", yscore + 1)
        else:
            print("You Lose")
            print("Opponent Score:-", oscore + 1)
        a = str(input("If you want Type Yes/Y or If you want to Exit Type No/N:-"))
        if  a== "Yes" or a=="Y":
            continue   
        else:
            print("Your Score:-",yscore)
            print("Opponent Score:-",oscore)
            continue
    else:
        print("Number Should be Between 1 and 6")


        print("/n")
        