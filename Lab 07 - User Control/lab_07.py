import arcade

arcade.open_window(600, 600, "Drawing Example")


arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()
def main():
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

    def draw_trees(x, y):
        arcade.draw_rectangle_filled(100 + x, 320 + y, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_circle_filled(100 + x, 350 + y, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_rectangle_filled(200 + x, 320 + y, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_ellipse_filled(200+ x, 370 + y, 60, 80, arcade.csscolor.DARK_GREEN)
        arcade.draw_rectangle_filled(300 + x, 320 + y, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_arc_filled(300 + x, 340 + y, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)
        arcade.draw_rectangle_filled(400 + x, 320 + y, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_triangle_filled(400 + x, 400 + y, 370 + x, 320 + y, 430 +x, 320 + y, arcade.csscolor.DARK_GREEN)
        arcade.draw_rectangle_filled(500 + x, 320 + y, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_circle_filled(500 + x, 360 + y, 30, arcade.csscolor.DARK_GREEN)


    def draws_sun(a, b):
        arcade.draw_circle_filled(500 + a, 550 + b, 40, arcade.color.YELLOW)
        arcade.draw_line(500 + a, 550 + b, 400 + a, 550 + b, arcade.color.YELLOW, 3)
        arcade.draw_line(500 + a, 550 + b, 600 + a, 550 + b, arcade.color.YELLOW, 3)
        arcade.draw_line(500 + a, 550 + b, 500 + a, 450 + b, arcade.color.YELLOW, 3)
        arcade.draw_line(500 + a, 550 + b, 500 + a, 650 + b, arcade.color.YELLOW, 3)
        arcade.draw_line(500 + a, 550 + b, 550 + a, 600 + b, arcade.color.YELLOW, 3)
        arcade.draw_line(500 + a, 550 + b, 550 + a, 500 + b, arcade.color.YELLOW, 3)
        arcade.draw_line(500 + a, 550 + b, 450 + a, 600 + b, arcade.color.YELLOW, 3)
        arcade.draw_line(500 + a, 550 + b, 450 + a, 500 + b, arcade.color.YELLOW, 3)

    draws_sun(-40, -60)
    draw_trees(0, -130)
    draw_trees(0, -250)
    draw_trees(0,0)
main()
arcade.finish_render()

arcade.run()