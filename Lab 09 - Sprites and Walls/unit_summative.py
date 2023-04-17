print("Find the key and unlock the door but make sure that you are ready to fight the dragon. \nYou will need camoflauge clothes, a sword, and food to refuel. ")

class Room():
    def __init__(self,description, north, east, south, west, locked):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.locked = locked


class Item():
    def __init__(self, short_name, long, room_number, use):
        self.short_name = short_name
        self.long = long
        self.use = use
        self.room_number = room_number
        




def main():
    room_list = []

    bathroom = Room("You are in bathroom 1. \nThere is a door to the north and east.", 9, 1, None, None, False) 
    room_list.append(bathroom)
    bedroom = Room("You are in bedroom 1. \nThere is a door to the north, east, and west.", 8, 2, None, 0, False)
    room_list.append(bedroom)
    southhallway = Room("You are in the south hallway. \nThere is a door to the north, east, and west.", 7, 3, None, 1, False)
    room_list.append(southhallway)
    kitchen = Room("You are in the kitchen. \nThere is a door to the north and west.", 4, None, None,2, False)  
    room_list.append(kitchen)
    livingroom = Room("You are in the living room. \nThere is a door to the north, south, and west.", 5, None,3,7, False)
    room_list.append(livingroom)
    diningroom = Room("You are in the dining room. \nThere is a door to the north, south, and west.",6, None, 4, 10, False)
    room_list.append(diningroom)
    bedroom2 = Room("You are in bedroom 2. \nThere is a door to the south.", None, None,5, None, False)
    room_list.append(bedroom2)
    northhallway = Room("You are in the north hallway. \nThere is a door to the north, east, south, and west.", 10, 4, 2, 8, False)
    room_list.append(northhallway)
    bedroom3 = Room("You are in bedroom 3. \nThere is a door to the east, south and west.", None,7,1,9, False)
    room_list.append(bedroom3)
    bathroom3 = Room("You are in bathroom 3. \nThere is a door to the east and south.", None, 8, 0, None, False)
    room_list.append(bathroom3)
    balcony = Room("You are on the balcony. \nThere is a door to the south.", None, None, 7, None, True)
    room_list.append(balcony)
    current_room = 0
    key =  Item("key", "There is a key in this room", 2, "used the key unlock the door")
    sword = Item("sword", "There is a sword in this room", 5, "used the sword to kill the dragon")
    food = Item("rusty", "There is food in here", 3, "I ate the food to refuel.")
    clothes = Item("clothes", "There is camoflauge clothes in this room", 8, "used the clothes to change my camoflauge outfit")


    items=[]
    items.append(key)
    items.append(sword)
    items.append(food)
    items.append(clothes)
    done=False
    x=0
    items_held=[]
    
    
    
    
        
    print()
    print(room_list[current_room].description)


    while done != True:
        x=0
        while x<4:  
            if items[x].room_number == current_room:
                print(items[x].long)
                break   
            x+=1
        if current_room == 10:
            user_inputs = input("Are you ready to fight the dragon?")
            if user_inputs == "yes":
                for item in items:
                    if item.room_number == -1:
                        print("i have tiems")




        user_input = input("What would you like to do? ")
        print()

        


        command_words = user_input.split(" ")
        if command_words[0] == "grab":
            print("I picked up the",items[x].short_name)
            items_held=items[x]
            items[x].room_number = -1
            continue 
        
        if command_words[0] == "use":
            for item in items:
                #print (item)
                #print(command_words[1])
                if item.short_name == command_words[1]:
                    print("I",item.use)
                    if command_words[1] == "key":
                        room_list[next_room].locked = False
            continue 

        if command_words[0]== "drop":
            for item in items:
                if command_words[1] == item.short_name:
                    if item.room_number == -1:
                        item.room_number = current_room
                        break
            else:
                print("You do not have this item.")
                    
        

        if command_words[0] == "inventory":            
            for item in items:
                if item.room_number == -1:
                    print(item.short_name)
            continue 
          
        
        if room_list[current_room] == True:
            print("You cannot go this way")
        
        
        if user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue
            room_lock = room_list[next_room].locked
            if room_lock == True:
                print("This room is locked. Find the key and come back to unlock")
            if room_lock == False:
                print(room_list[next_room].description)
                current_room = next_room
  
            continue
        

        elif user_input.lower()=="south":
            next_room = room_list[current_room].south
            
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue

            room_lock = room_list[next_room].locked
            if room_lock == True:
                print("This room is locked. Find or use the key to unlock.")
            if room_lock == False:
                print(room_list[next_room].description)
                current_room = next_room



            continue


        elif user_input.lower()=="east":   
            next_room = room_list[current_room].east
            
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue

            room_lock = room_list[next_room].locked
            if room_lock == True:
                print("find the key and come back")
            if room_lock == False:
                print(room_list[next_room].description)
                current_room = next_room
            continue


        elif user_input.lower()=="west":
            next_room = room_list[current_room].west
            
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue
            
            room_lock = room_list[next_room].locked
            if room_lock == True:
                print("find the key and come back")
            if room_lock == False:
                print(room_list[next_room].description)
                current_room = next_room


        elif user_input.lower()=="quit":
            break

        


main()
