import arcade
import random

class Rectangle():
    def __init__(self):
        self.x = random.randrange(0, 700)
        self.y = random.randrange(0, 500)
        self.height = random.randrange(20,70)
        self.width = random.randrange(20,70)
        self.color = [0,255,0]
        self.change_x = random.randrange(-3,3)
        self.change_y = random.randrange(-3,3)   
    def move(self): 
        self.x += self.change_x
        self.y += self.change_y
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.height,self.width, self.color)
class Ellipse(Rectangle):
    
    def draw(self):
        arcade.draw_ellipse_filled()
my_list = []
for x in range(10):
    my_object = Rectangle()
    my_ellipse = Ellipse()
my_list.append(my_object)
my_list.append(my_ellipse)

def main():
    arcade.open_window(700, 700, "Window")
    for list in my_list:
        my_ellipse.draw()
        my_object.move()
        my_object.draw()
    arcade.run()
main()        