class Room():
    def _init_(self,description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.south = west


def main():
    room = Room("bathroom", 9, 1, None, None)
    room_list = []
    room_list.append(room)
    
    print(room_list)

main()
