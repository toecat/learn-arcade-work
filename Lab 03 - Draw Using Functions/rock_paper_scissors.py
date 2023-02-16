import random
x = random.randrange(0,3)
if x==1:
    x="rock"
if x==0:
    x="paper"
if x==2:
    x="scissors"
def computer():
    print("The computer chose", x)
i = str(input("Choose rock, paper, or scissors: "))

if i.lower()==x:
    print("The computer had the same as you. Please choose another one: ")
    i = str(input("Choose rock, paper, or scissors: "))
if x=="rock" and i.lower()=="scissors":
    computer()
    print("The computer won")
elif x=="scissors" and i.lower()=="paper":
    computer()
    print("The computer won")
elif x=="paper" and i.lower()=="rock":
    computer()
    print("The computer won")
elif x=="scissors" and i.lower()=="rock":
    computer()
    print("You won")
elif x=="paper" and i.lower()=="scissors":
    computer()
    print("You won")
elif x=="rock" and i.lower()=="paper":
    computer()
    print("You won")
elif i.lower()==x:
    print("The computer had the same as you. Please choose another one: ")
    i = str(input("Choose rock, paper, or scissors: "))


