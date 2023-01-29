import arcade
arcade.open_window(800, 800, "Dog")
arcade.set_background_color(arcade.csscolor.WHITE)
arcade.start_render()
# draws head
arcade.draw_circle_filled(400, 400, 200, arcade.color.BEAVER)
arcade.draw_circle_outline(400, 400, 200, arcade.color.BLACK_BEAN)
# draws ears
arcade.draw_ellipse_filled(240, 300, 100, 420, arcade.color.BEAVER)
arcade.draw_ellipse_filled(560, 300, 100, 420, arcade.color.BEAVER)
arcade.draw_ellipse_outline(240, 300, 100, 420, arcade.color.BLACK_BEAN)
arcade.draw_ellipse_outline(560, 300, 100, 420, arcade.color.BLACK_BEAN)
# draws eyes
arcade.draw_circle_filled(350, 450, 40, arcade.color.WHITE)
arcade.draw_circle_filled(450, 450, 40, arcade.color.WHITE)
arcade.draw_circle_filled(350, 450, 20, arcade.color.BLACK)
arcade.draw_circle_filled(450, 450, 20, arcade.color.BLACK)
# draws nose
arcade.draw_ellipse_filled(400, 380, 100, 50, arcade.color.PINK)
arcade.draw_line(400, 300, 400, 400, arcade.color.PINK, 3)
arcade.draw_arc_outline(400, 335, 70, 70, arcade.csscolor.PINK, 180, 360, border_width=5)
arcade.finish_render()
arcade.run()
