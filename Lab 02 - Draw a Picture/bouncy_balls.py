import arcade
SCREEN_WIDTH=800
SCREEN_HEIGHT=800

def draw_dog(x,y):
    arcade.draw_ellipse_filled(400+x, 400+y, 200, 100, arcade.color.BEAVER)
    arcade.draw_line(350+x, 400+y, 350+x, 315+y, arcade.color.BEAVER, 5)
    arcade.draw_line(450+x, 400+y, 450+x, 315+y, arcade.color.BEAVER, 5)
    arcade.draw_line(340+x, 400+y, 340+x, 315+y, arcade.color.BEAVER, 5)
    arcade.draw_line(460+x, 400+y, 460+x, 315+y, arcade.color.BEAVER, 5)
    arcade.draw_circle_filled(500+x, 440+y, 40, arcade.color.BEAVER)
def draw_ball(x, y, z):
    arcade.draw_circle_filled(x, y, 10, z)
def on_draw(delta_time):
    arcade.start_render()
    draw_ball(on_draw.ball_x, 450, arcade.csscolor.YELLOW)
    draw_dog(on_draw.dog_x, 0)
    
    
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
