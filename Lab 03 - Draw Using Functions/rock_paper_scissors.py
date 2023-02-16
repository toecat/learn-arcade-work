import random
x = random.randrange(0,3)
if x==1:
    x="rock"
if x==0:
    x="paper"
if x==2:
    x="scissors"
i = str(input("Choose rock, paper, or scissors: "))
if i.lower()==x:
    print("The computer had the same as you. Please choose another one: ")
    i = str(input("Choose rock, paper, or scissors: "))
if x=="rock" and i.lower()=="scissors":
    print("The computer chose rock")
    print("The computer won")
if x=="scissors" and i.lower()=="paper":
    print("The computer chose scissors")
    print("The computer won")
if x=="paper" and i.lower()=="rock":
    print("The computer chose paper")
    print("The computer won")
if x=="scissors" and i.lower()=="rock":
    print("The computer chose scissors")
    print("You won")
if x=="paper" and i.lower()=="scissors":
    print("The computer chose paper")
    print("You won")
if x=="rock" and i.lower()=="paper":
    print("The computer chose rock")
    print("You won")

