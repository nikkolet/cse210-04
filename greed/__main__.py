from gc import collect
import os
import random

from game.casting.game_object import GameObject
from game.casting.collection import Collection

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.casting.falling_object import FallingObject

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
FLOOR = 580
CELL_SIZE = 20
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Greed"
#DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_FALLING_OBJECTS = 40


def main():
    
    # create the collection
    collection = Collection()
    
    # create the banner
    banner = GameObject()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    collection.add_game_object("banners", banner)
    
    # create the player
    x = int(MAX_X / 2)
    y = FLOOR
    position = Point(x, y)

    player = GameObject()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    collection.add_game_object("players", player)

    for obj in range(DEFAULT_FALLING_OBJECTS):
        n = obj % 2
        if(n == 0):
            text = "*"
        
        if(n != 0):
            text = "O"
        print(f"this is {text}")
        x = random.randint(1, MAX_X)
        # y = FONT_SIZE
        y = random.randint(1, MAX_Y)
        position = Point(x, y)
        #position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        falling_object = FallingObject()
        falling_object.set_text(text)
        falling_object.set_font_size(FONT_SIZE)
        falling_object.set_color(color)
        falling_object.set_position(position)

        if (text == "O"):
            falling_object.set_points(-1)
        
        if (text =="*"):
            falling_object.set_points(2)

        collection.add_game_object("falling_objects", falling_object)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service, collection)
    director.start_game()


if __name__ == "__main__":
    main()