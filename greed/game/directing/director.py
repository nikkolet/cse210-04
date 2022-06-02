from game.shared.point import Point
import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service, collection):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            collection (collection): The collection of actors.
        
        Attributes:
            floor(int): This is the floor where the player stands and the falling objects should be gone when touch
            points: This is the current points of the player
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._floor = 585
        self._collection = collection
        self._points = 00
        
    def start_game(self):
        """Starts the game using the given collection. Runs the main game loop.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(self._collection)
            self._do_updates(self._collection)
            self._do_outputs(self._collection)
        self._video_service.close_window()

    def _get_inputs(self, collection):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            collection (collection): The collection of actors.
        """
        player = collection.get_first_game_object("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, collection):
        """Updates the player's position and resolves any collisions with falling_objects.
        
        Args:
            collection (collection): The collection of actors.
        """
        banner = collection.get_first_game_object("banners")
        player = collection.get_first_game_object("players")
        falling_objects = collection.get_game_objects("falling_objects")

        banner.set_text(f"Score: {self._points}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for falling_object in falling_objects:
            if player.distance(falling_object.get_position()) < 20:
                self._points += falling_object.get_points()
                collection.remove_game_object("falling_objects", falling_object)
        
        #falling objects
        for falling_object in falling_objects: 
            velocity = Point(0,random.randint(8,15))
            falling_object.set_velocity(velocity)
            falling_object.move_next(max_x, max_y)

        
    def _do_outputs(self, collection):
        """Draws the actors on the screen.
        
        Args:
            collection (collection): The collection of actors.
        """
        self._video_service.clear_buffer()
        actors = collection.get_all_game_objects()
        self._video_service.draw_game_objects(actors)
        self._video_service.flush_buffer()

        