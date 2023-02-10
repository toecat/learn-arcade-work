import arcade
SCREEN_WIDTH=800
SCREEN_HEIGHT=800
def tree(a,b):
    arcade.draw_rectangle_filled(a, b, 60, 260, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(a, b+90, 90, arcade.csscolor.SEA_GREEN)
def draw_dog(x,y):
    arcade.draw_ellipse_filled(400+x, 400+y, 200, 100, arcade.color.BEAVER)
    arcade.draw_line(350+x, 400+y, 350+x, 315+y, arcade.color.BEAVER, 5)
    arcade.draw_line(450+x, 400+y, 450+x, 315+y, arcade.color.BEAVER, 5)
    arcade.draw_line(340+x, 400+y, 340+x, 315+y, arcade.color.BEAVER, 5)
    arcade.draw_line(460+x, 400+y, 460+x, 315+y, arcade.color.BEAVER, 5)
    arcade.draw_circle_filled(500+x, 440+y, 40, arcade.color.BEAVER)
    arcade.draw_circle_filled(510+x, 450+y, 9, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(510+x, 450+y, 6, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(480+x, 430+y, 30, 70, arcade.color.BEAVER)
    arcade.draw_ellipse_outline(480+x, 430+y, 30, 70, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(0, 799, 320, 0, arcade.csscolor.GREEN)
def draw_sun():
    arcade.draw_circle_filled(800, 800, 100, arcade.csscolor.YELLOW)

def draw_ball(x, y, z):
    arcade.draw_circle_filled(x, y, 10, z)
def on_draw(delta_time):
    arcade.start_render()
    draw_sun()
    tree(100, 400)
    tree(300, 400)
    tree(500, 400)
    tree(700, 400)
    
    draw_ball(on_draw.ball_x, 450, arcade.csscolor.YELLOW)
    draw_dog(on_draw.dog_x, 0)
    #draw_ball(on_draw.ball_x, 450, arcade.csscolor.PINK)

    
    on_draw.ball_x += 2
    on_draw.dog_x += 1


on_draw.dog_x = 0
on_draw.ball_x = 550

def main():
    arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT, "Window")
    arcade.set_background_color((48, 78, 240))
    arcade.schedule(on_draw, 1/60)
    
    
    arcade.run()

main()
