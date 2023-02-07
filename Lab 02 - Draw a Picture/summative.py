import arcade
arcade.open_window(900, 900,"Frog")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
def draws_frog():
    arcade.draw_ellipse_filled(200, 470, 100, 200, arcade.csscolor.GREEN, 30)
    arcade.draw_ellipse_filled(300, 500, 300, 200, arcade.csscolor.GREEN)
    arcade.draw_ellipse_filled(300, 500, 300, 200, arcade.csscolor.GREEN)


draws_frog()
arcade.finish_render()
arcade.run()