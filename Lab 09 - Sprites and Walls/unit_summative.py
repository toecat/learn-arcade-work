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
    bedroom2 = Room("You are in bedroom 2. \nThere is a door to the south.", None, None,5, None, True)
    room_list.append(bedroom2)
    northhallway = Room("You are in the north hallway. \nThere is a door to the north, east, south, and west.", 10, 4, 2, 8, False)
    room_list.append(northhallway)
    bedroom3 = Room("You are in bedroom 3. \nThere is a door to the east, south and west.", None,7,1,9, False)
    room_list.append(bedroom3)
    bathroom3 = Room("You are in bathroom 3. \nThere is a door to the east and south.", None, 8, 0, None, False)
    room_list.append(bathroom3)
    balcony = Room("You are on the balcony. \nThere is a door to the south.", None, None, 7, None, False)
    room_list.append(balcony)
    current_room = 0
    key =  Item("key", "There is a key in this room", 2, "used the key unlock the door")
    paper = Item("paper", "There is a paper in this room", 9, "made a paper airplane to fly")
    rusty_key = Item("rusty", "There is a rusty key on the balcony", 10, "used the key to unlock the door")
    clothes = Item("clothes", "There is clothes in this bedroom", 1, "used the clothes to change my outfit")


    items=[]
    items.append(key)
    items.append(paper)
    items.append(rusty_key)
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
                y=x
                break   
            x+=1
                
        user_input = input("What would you like to do? ")
        print()

        command_words = user_input.split(" ")
        if command_words[0] == "grab":
            print("I picked up the",items[x].short_name)
            items_held=items[x]
            items[x].room_number = -1
            continue 
        
        if command_words[0] == "use":
            print("I",items[y].use)
            items[y].locked = False
            continue 

        if command_words[0] == "inventory":            
            for item in items:
                if item.room_number == -1:
                    print(item.short_name)
            continue 
          
        
        if room_list[current_room] == True:
            print("you cannot go this way")
        
        
        if user_input.lower() == "north":
            next_room = room_list[current_room].north
            
            
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue
            print(room_list[current_room].description)
            room_lock = room_list[next_room].locked
            if room_lock == True:
                print("find the key and come back")
            else:
                current_room = next_room
  
            continue
        

        elif user_input.lower()=="south":
            next_room = room_list[current_room].south
            
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue
            print(room_list[current_room].description)
            room_lock = room_list[next_room].locked
            if room_lock == True:
                print("find the key and come back")
            else:
                current_room = next_room


            continue


        elif user_input.lower()=="east":   
            next_room = room_list[current_room].east
            
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue
            print(room_list[current_room].description)
            room_lock = room_list[next_room].locked
            if room_lock == True:
                print("find the key and come back")
            else:
                current_room = next_room
            continue


        elif user_input.lower()=="west":
            next_room = room_list[current_room].west
            
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue
            print(room_list[current_room].description)
            room_lock = room_list[next_room].locked
            if room_lock == True:
                print("find the key and come back")
            else:
                current_room = next_room

        elif user_input.lower()=="quit":
            break

        


main()
