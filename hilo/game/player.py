from types import new_class
from game.card import Card


class Player:
    """A person who directs the game. 
    
    The responsibility of a Player is to guess wether or not the next card
    will be higher than the current one. The Player also decides if they
    want to keep playing or finish the game with the current score.

    Attributes:
        current_card (int): The current card value (1-13)
        new_card (int): The value of the new card flipped (1-13)
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        self.current_card = Card().value
        self.is_playing = True
        self.score = 300
        self.high_low = ""

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Player): an instance of Player.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to flip a new card.

        Args:
            self (Player): An instance of Player.
        """
        print(f'The card is {self.current_card}')
        flip_card = input("Flip another card? [y/n] ")
        self.is_playing = (flip_card == "y")
        if self.is_playing:
            self.high_low = input("Will the next card be higher or lower? [h/l]")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Player): An instance of Player.
        """
        if not self.is_playing:
            return 

        print(f'The card is {self.current_card}')
        new_card = Card()

        if new_card.value > self.current_card:
            if self.high_low == "h":
                self.score += 100
            else:
                self.score -= 75
        elif new_card.value < self.current_card:
            if self.high_low == "l":
                self.score += 100
            else:
                self.score -= 75
        self.current_card = new_card.value

    def do_outputs(self):
        """Displays the new card and the score. Also asks the player if they want to roll again. 

        Args:
            self (Player): An instance of Player.
        """
        
        if not self.is_playing:
            return

        print(f"The new card is: {self.current_card}")
        print(f"Your score is: {self.score}\n")
        self.is_playing = (self.score > 0)
