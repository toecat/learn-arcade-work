import arcade
arcade.open_window(800, 800, "Dog")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 799, 400, 0, arcade.csscolor.LIGHT_GREEN )
arcade.draw_lrtb_rectangle_outline(0, 799, 400, 0, arcade.csscolor.GREEN, border_width=5 )

# draws tree
arcade.draw_rectangle_filled(700,400,60, 100, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((750, 450),
                            (800, 550),
                            (650, 450),
                            (650, 650),
                            ),
                            arcade.csscolor.GREEN)
arcade.draw_polygon_outline(((750, 450),
                            (800, 550),
                            (650, 450),
                            (650, 650),
                            ),
                            arcade.csscolor.DARK_GREEN)
#draws the sun
arcade.draw_circle_filled(100, 700, 40, arcade.color.YELLOW)

# draws head
arcade.draw_circle_filled(400, 400, 200, arcade.color.BEAVER)
arcade.draw_circle_outline(400, 400, 200, arcade.color.BLACK)
# draws ears
arcade.draw_ellipse_filled(235, 325, 100, 420, arcade.color.BEAVER)
arcade.draw_ellipse_filled(565, 325, 100, 420, arcade.color.BEAVER)
arcade.draw_ellipse_outline(235, 325, 100, 420, arcade.color.BLACK)
arcade.draw_ellipse_outline(565, 325, 100, 420, arcade.color.BLACK)
# draws eyes
arcade.draw_circle_filled(350, 450, 40, arcade.color.WHITE)
arcade.draw_circle_filled(450, 450, 40, arcade.color.WHITE)
arcade.draw_circle_filled(350, 450, 20, arcade.color.BLACK)
arcade.draw_circle_filled(450, 450, 20, arcade.color.BLACK)
# draws nose
arcade.draw_ellipse_filled(400, 380, 100, 50, arcade.color.PINK)
arcade.draw_line(400, 300, 400, 400, arcade.color.PINK, 3)
arcade.draw_arc_outline(400, 335, 70, 70, arcade.csscolor.PINK, 180, 360, border_width=5)
arcade.draw_arc_outline(400, 600, 400, 300, (250,0,0,127), 0, 180, 100, 0)
arcade.draw_arc_outline(400, 600, 400, 300, (240,10,10,117), 0, 180, 90, 0)

arcade.finish_render()
arcade.run()