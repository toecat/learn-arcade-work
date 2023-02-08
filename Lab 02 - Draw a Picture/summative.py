import arcade
arcade.open_window(900, 900,"Frog")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
def draws_frog():
    arcade.draw_ellipse_filled(300, 500, 300, 200, arcade.csscolor.GREEN)
    arcade.draw_ellipse_filled(170, 420, 80, 130, arcade.csscolor.GREEN, 30)
    #arcade.draw_ellipse_outline(200, 440, 50, 100, arcade.csscolor.BLACK, 2, 30)
    arcade.draw_ellipse_filled(190, 390, 130, 80, arcade.csscolor.GREEN)
    


draws_frog()
arcade.finish_render()
arcade.run()