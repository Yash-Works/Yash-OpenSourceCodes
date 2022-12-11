import random

a="Yes"
min = 1
max = 6
roll_again = "Yes"
yscore = 0
oscore = 0
print("Welcome To The Game")
while a=="Yes":
    num = int(input("Enter A Number(Only 1 to 6):->"))
    ran = random.randint(min,max)
    if 1<= num<=6:
        print("Dice Is Rolling ")
        print("The Generated Number is:->", ran)
        if num == ran:
            print("You Won")
            print("Your Score:->", yscore + 1)
            print("Opponent Score:->", oscore)
            yscore+=1
        else:
            print("You Lose")
            print("Your Score:->",yscore)
            print("Opponent Score:->", oscore + 1)
            oscore+=1
    a = str(input("If you want Type Yes or If you want to Exit Type No:-"))
    if  a== "Yes":
        continue 
    else:
        print("Your Score:-", yscore)
        print("Opponent Score:-",oscore)  
        break
    
        