import random

# TODO: Implement the Card class as follows...

# 1) Add the class declaration. Use the following class comment.
"""A card from a deck of cards with a value from 1 to 13.

    The responsibility of Card is to keep track of the value of the new card
    on the top of the deck.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """
class Card:
    # 2) Create the class constructor. Use the following method comment.
    """Constructs a new instance of Card with a value attribute.

            Args:
                self (Card): An instance of Card.
            """
    def __init__(self):
        self.value = random.randint(1, 13)
        
    # 3) Create the flip_card(self) method. Use the following method comment.
    """Generates a new random value between 1 and 13.

    Args:
        self (Card): An instance of Card.
    """
    def flip_card(self):
        self.value = random.randint(1, 13)