import arcade
import pathlib

WIDTH = 1000
HEIGHT = 650
TITLE = "Slime Game"

# Assets path
ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"

#set scale
CHARACTER_SCALE = 1.0
TILE = 1.0

#Player Constants
GRAVITY = 1
MOVMENT = 10
JUMP = 30

class Game(arcade.Window):
    def __init__(self) -> None:
        super().__init__(WIDTH, HEIGHT, TITLE)

        # load the diffrent objects
        self.tile_map = None
        self.scene = None
        self.player_sprite = None
        self.physics_engine = None
        self.camera = None
        self.gui_camera = None
        self.score = 0
        self.level = 1

        # Get the Diffrent Sounds
        self.jump_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "jump.wav")
        )
        self.victory_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "victory.wav")
        )
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.camera = arcade.Camera(WIDTH,HEIGHT)
        self.gui_camera = arcade.Camera(WIDTH,HEIGHT)
        
        map_name = ":resources:tiled_maps/map.json"
        
        layer_options = {
            "Platforms":{
                "use_spatial_hash":True,
            },
        }
        
        self.tile_map = arcade.load_tilemap(map_name,TILE,layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.score = 0
        
        #set up player
        image_source = ":resources:images/animated_characters/slime/slimePurple.png"
        self.player_sprite = arcade.Sprite(image_source,CHARACTER_SCALE)
        self.player_sprite.center_x = 175
        self.player_sprite.center_y = 200
        self.scene.add_sprite("Player",self.player_sprite)
        
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Platforms"]
        )

    def on_key_press(self, key: int, modifiers: int):
        """Called when you press a key """
        if key == arcade.key.LEFT or key == arcade.key.A:
            if self.physics_engine.can_jump():
                self.jump_sound.play()
                self.player_sprite.change_y = JUMP
            elif self.physics_engine.can_jump()==False:
                self.player_sprite.change_x = -MOVMENT
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            if self.physics_engine.can_jump():
                self.jump_sound.play()
                self.player_sprite.change_y = JUMP
            else:
                self.player_sprite.change_x = MOVMENT
            
    def on_key_release(self, key: int, modifiers: int):
        """Called when you release a key"""
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
            
    def center_camera(self):
        screen_x = self.player_sprite.center_x - (self.camera.viewport_width/2)
        screen_y = self.player_sprite.center_y - (self.camera.viewport_height/2)
        if screen_x < 0:
            screen_x = 0
        if screen_y < 0:
            screen_y = 0
        player_centered = screen_x,screen_y
        self.camera.move_to(player_centered)
    
    def on_update(self,delta_time):
        if self.physics_engine.can_jump()==True:
            self.player_sprite.change_x = 0
        self.physics_engine.update()
        self.center_camera()
        
    
    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()
        self.gui_camera.use()
        score_text = f"Score:{self.score}"
        arcade.draw_text(
            score_text,10,10,arcade.csscolor.WHITE,18,
        )


if __name__ == "__main__":
    window = Game()
    window.setup()
    arcade.run()
