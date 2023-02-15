import random
print("Guess my number 1-100 in 10 tries!")
x = random.randrange(1,100)
num = int(input("What is your guess? "))
for i in range(10) :
    print("No")
    if x>num:
        print("Your guess was to small. ")
        num = int(input("What is your guess? "))

    if x<num:
        print("Your guess was to large. ")
        num = int(input("What is your guess? "))
    if num == x:
        print('Yes!')
        print("You guessed the number which was", x)
        quit()
if num != x: 
    print("You ran out of tries.")  
    print("You did not guess the number. The number was",x)

