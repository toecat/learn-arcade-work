import arcade
import random

class Rectangle():
    def __init__(self):
        self.x = random.randrange(0, 700)
        self.y = random.randrange(0, 500)
        self.height = random.randrange(20,70)
        self.width = random.randrange(20,70)
        self.color = [random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)]
        self.change_x = random.randrange(-3,3)
        self.change_y = random.randrange(-3,3)   
    
    def move(self): 
        self.x += self.change_x
        self.y += self.change_y
        
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.height,self.width, self.color)


class Ellipse(Rectangle):  
    pass 

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.height, self.width, self.color)


def main():
    arcade.open_window(700, 700, "Window")
    
    arcade.start_render()
    
    my_list = []
    for x in range(30):
        my_object = Rectangle()
        my_ellipse = Ellipse()
        my_object.draw()
        my_ellipse.draw()
    my_list.append(my_object)
    my_list.append(my_ellipse)
    
    arcade.run()
    arcade.finish_render()


main()        
