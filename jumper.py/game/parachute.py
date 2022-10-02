"""A parachute drawing that reveals how many lives the player has left.

Its responsibility is to keep track of the lives left and update it if the player's guess is incorrect.

atrributes:
_lives (int): The amount of lives left
_drawing: (string): The drawing of the parachute displayed in screen
"""
class Parachute:     

    """Constructs a new Seeker.

    Args:
        self (Seeker): An instance of Parachute.
    """
    def __init__(self):
        self._lives = 4
        self._drawing = [' ___ ', '/___\\', '\   /', ' \ /', '  o  ', ' /|\\', ' / \\']

    def reduce_life(self):
        """Reduces the lives in 1

        Args: 
            self (Parachute): An instance of Parachute.
        """

        self._lives -= 1

    def update_drawing(self):
        """Removes one line from the top of the drawing

        Args: 
            self (Parachute): An instance of Parachute.
        """
        if self._lives > 0:
            self._drawing.pop(0)
        else:
            self._drawing = ['  x  ', ' /|\\', ' / \\']

    def print_drawing(self):
        """Prints the drawing

        Args: 
            self (Parachute): An instance of Parachute.
        """
        for i in self._drawing:
            print(i)