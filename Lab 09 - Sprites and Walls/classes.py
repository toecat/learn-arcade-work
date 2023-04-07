import arcade
import random

class Rectangle():
    def __init__(self,x,y,width,height,change_x,change_y,color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.change_x = change_x
        self.change_y = change_y  

    
    def move(self): 
        self.x += self.change_x
        self.y += self.change_y
        
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width,self.height, self.color)


class Ellipse(Rectangle):  
    pass 

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.height, self.width, self.color)

class Shapes(arcade.Window):
    def _init_(self):
        super()._init_(700,700,"Window")
        self.my_list=None
    
    def setup(self):
        self.my_list=[]
        for x in range(52):
            x=random.randrange(0,700)
            y=random.randrange(0,500)
            height=random.randrange(20,70)
            width=random.randrange(20,70)
            change_x=random.randrange(-3,3)
            change_y=random.randrange(-3,3)

            todraw = random.randrange(1,3)
            if todraw == 1:
                my_object = Rectangle(x+random.randrange(25),y,width,height,change_x,change_y,[random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)])
                self.my_list.append(my_object)
            if todraw == 2:
                my_ellipse = Ellipse(x,y+random.randrange(70),width,height,change_x,change_y,[random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)])
                self.my_list.append(my_ellipse)
    
    
    def update(self,dt):
        for shapes in self.my_list:
            shapes.move()
    
    
    def on_draw(self):
        arcade.start_render()
        for shape in self.my_list:
            shape.draw()
    
   
window=Shapes()
window.setup()
arcade.run()



      
