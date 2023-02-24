print("The sharks are trying to catch you! ")
print("Move 300 miles to a safe spot before they catch you!")
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
        sharks = random.randrange(0, 10)
        full_speed = random.randrange(10, 20)
        moderate_speed = random.randrange(5, 12)
        print ("Miles traveled:", miles_traveled)
        print("Food in backpack:", eat)
        print("shark_travel:", shark_travel)
        print("The sharks are", (miles_traveled-shark_travel), "behind you.")
        print("Tiredness:", fish_tired)
        print("Hunger level is:", hunger) 
    elif choice == "d":
        sharks = random.randrange(0, 10)
        full_speed = random.randrange(10, 20)
        moderate_speed = random.randrange(5, 12)
        fish_tired = 0
        print ("The fish is happy! And the sharks have moved", sharks, "miles while you were stoped" )
        eat = 7
    elif choice == "c":
        sharks = random.randrange(0, 10)
        full_speed = random.randrange(10, 20)
        moderate_speed = random.randrange(5, 12)
        print ("You have traveled", full_speed, "miles" )
        miles_traveled = miles_traveled + full_speed
        shark_travel +=  sharks
        print("shark_travel:", shark_travel)
        hunger += 1
        fish_tired = fish_tired+random.randrange(1,3)
        print ("The sharks are" , miles_traveled-shark_travel,"miles behind you")
        print("You have moved", miles_traveled,"miles in total.")
    elif choice == "b":
        sharks = random.randrange(0, 10)
        full_speed = random.randrange(10, 20)
        moderate_speed = random.randrange(5, 12)
        print ("You have traveled",moderate_speed, "miles")
        miles_traveled += full_speed
        shark_travel += sharks
        print ("shark_travel:", shark_travel)
        hunger += 1
        fish_tired = fish_tired + random.randrange(1,3)
        print ("Fish tiredness: ", fish_tired)
        print ("The sharks are", miles_traveled-shark_travel,"miles behind you.")
        print("You have moved", miles_traveled,"miles in total.")
    elif choice == "a":
        sharks = random.randrange(0, 10)
        full_speed = random.randrange(10, 20)
        moderate_speed = random.randrange(5, 12)
        print ("You ate from your backpack")
        eat = eat - 1
        hunger = 0
    
    if hunger >= 5:
        print ("You died of hunger.")
        done=True
        break
    if hunger >= 3 :
        print ("You are hungry. Eat from your backpack.")

    if fish_tired >= 6:
        print ("Your fish is dead")
        done = True
    if fish_tired >= 4:
        print ("Your fish is tired. You better take a break.")
    if shark_travel >= miles_traveled:
        print ("The sharks caught you")
        done = True
        break
    if shark_travel >= miles_traveled-10:
        print ("The sharks getting close")
    if miles_traveled >= 300:
        print ("You won!")
        done = True
        break
    if eat <= 0:
        print ("You are out of food.")
        hunger = 0
        eat = done
    
        

    
    