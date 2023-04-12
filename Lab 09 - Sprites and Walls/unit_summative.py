class Room():
    def __init__(self,description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    bathroom = Room("You are in bathroom 1. There is a door to the north and east.", 9, 1, None, None) 
    bedroom = Room("You are in bedroom 1. There is a door to the north, east, and west.", 8, 2, None, 0)
    southhallway = Room("You are in the south hallway. There is a door to the north, east, and west.", 7, 3, None, 1)
    kitchen = Room("You are in the kitchen. There is a door to the north and west.", 4, None, None,2)  
    livingroom = Room("You are in the living room. There is a door to the north, south, and west.", 5, None,3,7)
    diningroom = Room("You are in the dining room. There is a door to the north, south, and west.",6, None, 4, 10)
    bedroom2 = Room("You are in bedroom 2. There is a door to the south.", None, None,5, None)
    northhallway = Room("You are in the north hallway. There is a door to the north, east, south, and west.", 10, 4, 2, 8)
    bedroom3 = Room("You are in bedroom 3. There is a door to the east, south and west.", None,7,1,9)
    bathroom3 = Room("You are in bathroom 3. There is a door to the east and south.", None, 8, 0, None)
    balcony = Room("You are on the balcony. There is a door to the south.", None, None, 7, None)
    room_list = []
    room_list.append(bathroom)
    room_list.append(bedroom)
    room_list.append(southhallway)
    room_list.append(kitchen)
    room_list.append(livingroom)
    room_list.append(diningroom)
    room_list.append(bedroom2)
    room_list.append(northhallway)
    room_list.append(bedroom3)
    room_list.append(bathroom3)
    room_list.append(balcony)
    current_room = 0
    done=False
    while done != True:
        print()
        print(room_list[current_room].description)

        user_input = input("Where would you like to go?")



        if user_input.lower() == "north":
            next_room = room_list[current_room].north
            
            print(next_room)
            if next_room == None:
                print("You cannot go that way.")
            current_room = next_room
            print(current_room)
            print(room_list[current_room].description)


        elif user_input.lower()=="south":
            next_room = room_list[current_room].south
            print("south")
            if next_room == None:
                print("You cannot go that way.")
            current_room = next_room


        elif user_input.lower()=="east":
            
            next_room = room_list[current_room].east
            if next_room == None:
                print("You cannot go that way.")
            current_room = next_room
            print(room_list[current_room].description)


        elif user_input.lower()=="west":
            next_room = room_list[current_room].west
            print("west")
            if next_room == None:
                print("You cannot go that way.")
            current_room = next_room



main()
