"""The player. 
    
    The responsibility of a Player is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Player (1-1000).
    """

class Player:

    """Constructs a new Player.

    Args:
        self (Player): An instance of Player.
    """
    def __init__(self):              
        self._location = 0
       
    """Gets the current location.
    
    Returns:
        number: The current location,
    """
    def get_location(self):
        location = self._location
        return location

        
# 4) Create the move_location(self, location) method. Use the following method comment.
    """Moves to the given location.

    Args:
        self (Player): An instance of Player.
        location (int): The given location.
    """
    def move_location(self, location):
        self._location = location