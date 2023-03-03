import arcade
def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)
    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)

def draw_section_1():
    y=-5
    x=0
    for row in range(30):
        y+=10
        x=5
        for column in range(60):
            if column%2==0:    
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x+=5

def draw_section_2():
    y=-5
    x=0
    for row in range(30):
        y+=10
        x=305
        for column in range(30):
            if column%2==0:    
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
                x+=10
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            x+=5

    pass
def draw_section_3():
    y=-5
    x=0
    for row in range(30):
        y+=10
        x=605
        for column in range(30):
            if row%2==0:
                arcade.draw_rectangle_filled(x, y+10, 5, 5, arcade.color.BLACK)  
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
                x+=10
        x+=5
    pass
def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    y=5
    
    x=905
    for i in range (15):
        for row in range(15):
              
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)  
            arcade.draw_rectangle_filled(x, y+10, 5, 5, arcade.color.BLACK)  
            y+=20
        y=5
        for column in range(30):
            
            arcade.draw_rectangle_filled(x+10, y, 5, 5, arcade.color.BLACK)
            y+=10
        x+=20
        y=5
def draw_section_5():
    pass
def draw_section_6():
    pass
def draw_section_7():
    pass
def draw_section_8():
    pass
def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
    
    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()
    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()
    arcade.finish_render()
    arcade.run()
main()