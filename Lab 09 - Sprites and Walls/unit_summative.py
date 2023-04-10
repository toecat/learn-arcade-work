class Room():
    def __init__(self,description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.south = west


def main():
    bathroom = Room("bathroom 1", 9, 1, None, None) 
    bedroom = Room("bedroom 1", 8, 2, None, 0)
    southhallway = Room("south hallway", 7, 3, None, 1)
    kitchen = Room("kitchen", 4, None, None,2)  
    livingroom = Room("living room", 5, None,3,7)
    diningroom = Room("dining room",6, None, 4, 10)
    bedroom2 = Room("bedroom 2", None, None,5, None)
    northhallway = Room("north hallway", 10, 4, 2, 8)
    bedroom3 = Room("bedroom 3", None,7,1,9)
    bathroom3 = Room("bathroom 3", None, 8, 0, None)
    balcony = Room("balcony", None, None, 7, None)
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
    user_input = input("Where would you like to go?")
    if user_input == "north"():
        print("hello")
    while done != True:
        print()
        print(room_list[current_room].description)
        done = True
    #next_room = room_list(current_room).north


main()
