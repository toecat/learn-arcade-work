

def bedtimestory(animal_list,current,number): 
    print(animal_list [current],"went to bed after reading a story to the", animal_list[current+1])                  
    if current == number:
        return
    bedtimestory(animal_list,current+1,number)                   
    print("and then the ", animal_list[current], "fell asleep.")                  
   

def main(): 

    animal_list  = ["Mother","Sloth", "Dolphin", "Turtle", "Dog"]                
    bedtimestory(animal_list, 0, 3);

main()