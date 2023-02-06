import arcade
arcade.open_window(600, 600, "Colorful Trees")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
def main():
    
    #draws the grass
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
    def draw_tree(x, y, t, l, a, b, c, d):
        arcade.draw_rectangle_filled(x, y, t, l, arcade.csscolor.SIENNA)
        arcade.draw_circle_filled(a, b, c, d )


    def draw_sun():
        arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
        arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)


    draw_tree(470, 300, 40, 80, 470, 370, 60, arcade.csscolor.SALMON)
    draw_tree(100, 270, 40, 100, 100, 340, 60, arcade.csscolor.PINK)
    draw_tree(270, 300, 40, 90, 270, 370, 60, arcade.csscolor.BLUE_VIOLET)
    draw_tree(200, 170, 40, 85, 200, 240, 60, arcade.csscolor.ORANGE_RED)
    draw_tree(500, 170, 40, 85, 500, 240, 60, arcade.csscolor.LIGHT_YELLOW)
    draw_tree(350, 140, 40, 85, 350, 220, 60, arcade.csscolor.MEDIUM_PURPLE)
    draw_tree(90, 115, 40, 85, 90, 185, 60, arcade.csscolor.LIGHT_SEA_GREEN)
    draw_sun()
main()
arcade.finish_render()
arcade.run()