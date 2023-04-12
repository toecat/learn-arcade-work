class Room():
    def __init__(self,description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

class Item():
    def __init__(self, short_name, long, room_number):
        items = ["beach ball", "shovel", 'bucket', "goggles"]
        self.short_name = short_name
        self.long = long
        self.room_number = room_number
        short_name = items[0]



def main():
    room_list = []

    bathroom = Room("You are in bathroom 1. There is a door to the north and east.", 9, 1, None, None) 
    room_list.append(bathroom)
    bedroom = Room("You are in bedroom 1. There is a door to the north, east, and west.", 8, 2, None, 0)
    room_list.append(bedroom)
    southhallway = Room("You are in the south hallway. There is a door to the north, east, and west.", 7, 3, None, 1)
    room_list.append(southhallway)
    kitchen = Room("You are in the kitchen. There is a door to the north and west.", 4, None, None,2)  
    room_list.append(kitchen)
    livingroom = Room("You are in the living room. There is a door to the north, south, and west.", 5, None,3,7)
    room_list.append(livingroom)
    diningroom = Room("You are in the dining room. There is a door to the north, south, and west.",6, None, 4, 10)
    room_list.append(diningroom)
    bedroom2 = Room("You are in bedroom 2. There is a door to the south.", None, None,5, None)
    room_list.append(bedroom2)
    northhallway = Room("You are in the north hallway. There is a door to the north, east, south, and west.", 10, 4, 2, 8)
    room_list.append(northhallway)
    bedroom3 = Room("You are in bedroom 3. There is a door to the east, south and west.", None,7,1,9)
    room_list.append(bedroom3)
    bathroom3 = Room("You are in bathroom 3. There is a door to the east and south.", None, 8, 0, None)
    room_list.append(bathroom3)
    balcony = Room("You are on the balcony. There is a door to the south.", None, None, 7, None)
    room_list.append(balcony)
    current_room = 0
    done=False
    
    print()
    print(room_list[current_room].description)


    while done != True:
        user_input = input("Where would you like to go? ")
        print()

        if user_input.lower() == "north":
            next_room = room_list[current_room].north
            
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue
            current_room = next_room
            print(room_list[current_room].description)
            continue


        elif user_input.lower()=="south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue
            current_room = next_room
            print(room_list[current_room].description)

            continue


        elif user_input.lower()=="east":
            
            next_room = room_list[current_room].east
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue
            current_room = next_room
            print(room_list[current_room].description)
            continue


        elif user_input.lower()=="west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You cannot go that way.")
                print()
                continue
            current_room = next_room
            print(room_list[current_room].description)

            continue
        elif user_input.lower()=="quit":
            break


main()
