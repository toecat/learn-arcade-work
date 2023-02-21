print("Welcome to Fish!")
import random
done = False
miles_traveled = 0
hunger = 0
fish_tired = 0
shark_travel = -10
eat = 7
sharks = random.randrange(0, 10)
full_speed = random.randrange(10, 20)
moderate_speed = random.randrange(5, 12)

while not done:
    print("A. Eat from your backpack .")
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
        print("Food in backpack:", eat)
        print("The sharks are", (miles_traveled-shark_travel), "behind you.")
        print("Tiredness:", fish_tired)
        print("Hunger level is:", hunger) 
    elif choice == "d":
        fish_tired = 0
        print ("The fish is happy! And the sharks have moved", sharks, "miles while you were stoped" )
        eat = 7
    elif choice == "c":
        print ("You have traveled", full_speed, "miles" )
        miles_traveled = miles_traveled + full_speed
        shark_travel = shark_travel +  sharks
        hunger = hunger + 1
        fish_tired = random.randrange(1,3)
        print ("The sharks haved moved", shark_travel, "miles in total.")
        print("You have moved", miles_traveled,"miles in total.")
    elif choice == "b":
        print ("you have traveled",moderate_speed, "miles")
        miles_traveled += full_speed
        shark_travel += sharks
        hunger += 1
        fish_tired = fish_tired + random.randrange(1,3)
        print ("Fish tiredness: ", fish_tired)
        print ("The sharks have moved", shark_travel,"miles in total.")
        print("You have moved", miles_traveled,"miles in total.")
    elif choice == "a":
        print ("You ate from your backpack")
        eat = eat - 1
        hunger = 0
    
    if hunger >= 5:
        print ("You died of hunger.")
        done=True
    if hunger >= 3 :
        print ("You are hungry. Eat from your backpack.")

    if fish_tired >= 8:
        print ("Your fish is dead")
        done = True
    if fish_tired >= 5:
        print ("Your fish is tired. You better take a break.")
    if shark_travel >= miles_traveled:
        print ("The sharks caught you")
        done = True
    if shark_travel >= miles_traveled-10:
        print ("The sharks getting close")
    if miles_traveled >= 300:
        print ("You won!")
        done = True
    if eat <= 0:
        print ("You are out of food.")
        hunger = 0
        eat = done
    
        

    
    