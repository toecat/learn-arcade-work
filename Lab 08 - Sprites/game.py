import arcade

screen_width = 1000
screen_height = 650
screen_title = "Platformer"

CHARACTER_SCALING = 1
TILE_SCALING = 1
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, screen_title)
        self.wall_list = None
        self.player_list = None
        self.player_sprite = None
        arcade.set_background_color(arcade.csscolor.ALICE_BLUE)

        def setup(self):
            self.player_list = arcade.SpriteList()
            self.wall_list = arcade.SpriteList(use_spatial_hash=True)

            image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
            self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
            self.player_sprite.center_x = 64
            self.player_sprite.center_y = 128
            self.player_list.append(self.player_sprite)

            for x in range(0, 1250, 64):
                wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
                wall.center_x = x
                wall.center_y = 32
                self.wall_list.append(wall)

            coordinate_list = [[512, 96], [256, 96], [768, 96]]

            for coordinate in coordinate_list:
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
                wall.position = coordinate
                self.wall_list.append(wall)

            

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.player_list.draw()

def main():
    window = MyGame()
    window.setup()
    arcade.run()    

if __name__ == "__main__":
    main()
