print("Welcome to Camel!")
import random
done = False
miles_traveled = 0
thirst = 0
camel_tired = 0
bandits_travel = -20
drink = 7
bandits = random.randrange(0, 10)
full_speed = random.randrange(10, 20)
moderate_speed = random.randrange(5, 12)

while not done:
    print("A. Drink from your canteen .")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    choice = input("Your choice? ")
    
    
    if choice.lower() == "q":
        done = True
    elif choice == "e":
        print ("Miles traveled:", miles_traveled)
        print("Drinks in canteen:", drink)
        print("The bandits are", (miles_traveled-bandits_travel), "behind you.")
        print("Tiredness:", camel_tired)
        print("Thirst level is:", thirst) 
    elif choice == "d":
        camel_tired = 0
        print ("The camel is happy! And the bandits have moved", bandits, "miles while you were stoped" )
        drink = 7
    elif choice == "c":
        print ("You have traveled", full_speed, "miles" )
        miles_traveled = miles_traveled + full_speed
        bandits_travel = bandits_travel +  bandits
        thirst = thirst + 1
        camel_tired = random.randrange(1,3)
        print ("Camel tiredness:", camel_tired)
        print ("The bandits haved moved", bandits_travel, "miles in total.")
        print("You have moved", miles_traveled,"miles in total.")
    elif choice == "b":
        print ("you have traveled",moderate_speed, "miles")
        miles_traveled += full_speed
        bandits_travel += bandits
        thirst += 1
        camel_tired = camel_tired + random.randrange(1,3)
        print ("Camel tiredness: ", camel_tired)
        print ("The bandits have moved", bandits_travel,"miles in total.")
        print("You have moved", miles_traveled,"miles in total.")
    elif choice == "a":
        print ("You drank from your canteen")
        drink = drink - 1
        thirst = 0
    if thirst >= 3 :
        print ("You are thirsty. Drink water.")
    if thirst >= 5 :
        print ("You died of thirst.")
        done = True
    if camel_tired >= 5:
        print ("Your camel is tired. You better take a break.")
    if camel_tired >= 8:
        print ("Your camel is dead")
        done = True
    if bandits_travel >= miles_traveled:
        print ("The bandits caught you")
        done = True
    elif bandits_travel >= miles_traveled-10:
        print ("The bandits getting close")
    if miles_traveled >= 300:
        print ("You won!")
        done = True
    if drink <= 0:
        print ("You are out of drinks.")
        thirst = 0
        drink = done
    
        

    
    