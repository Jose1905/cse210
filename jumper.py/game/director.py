from game.parachute import Parachute
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _puzzle (Puzzle): The hidden word.
        _is_playing (boolean): Whether or not to keep playing.
        _parachute (Parachute): The drawing displayed to show the amount of lives left.
        _letter (string): The letter selected by the player
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        self._parachute = Parachute()
        self._letter = ''
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        self._parachute.print_drawing()
        self._puzzle.print_display()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets the letter input by the player

        Args:
            self (Director): An instance of Director.
        """
        self._letter = input("\nEnter a letter: ")
        
    def _do_updates(self):
        """Verifies if the guess is correct

        Args:
            self (Director): An instance of Director.
        """
        guess = self._puzzle.verify_letter(self._letter)
        if guess == True:
            self._puzzle.update_display(self._letter)
        else:
            self._parachute.reduce_life()
            self._parachute.update_drawing()
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._parachute.print_drawing()
        self._puzzle.print_display()
        if self._puzzle.verify_victory():
            print('Congratulations! You won :D')
            self._is_playing = False
        elif self._parachute._lives == 0:
            print('You lost :c')
            self._is_playing = False