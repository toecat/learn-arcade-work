import arcade

class Rectangle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 10
        self.color = [0, 0, 255]
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.color)
my_object = Rectangle()
def main():
    arcade.run
main()        