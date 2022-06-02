from game.casting.game_object import GameObject


class FallingObject(GameObject):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        
    def get_points(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._points
    
    def set_points(self, points):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._points = points