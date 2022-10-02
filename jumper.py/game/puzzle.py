import random

class Puzzle:
    """The puzzle to solve. 
    
    The responsibility of Puzzle is to keep track of letters left to win
    
    Attributes:
        _word_list (list): A list of different words
        _selected_word (string): The hidden word selected to play with
        _display (string): The displayed spaces and letters for the player
    """

    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._word_list = ['ambulance', 'building', 'warlock', 'newspaper', 'ambassador']
        self._selected_word = self._word_list[random.randint(0, len(self._word_list))]
        self._display = ''
        for i in range(0, len(self._selected_word)):
            self._display += '_'
    
    def verify_letter(self, letter):
        """Verifies if the input letter is in the word.

        Args:
            self (Puzzle): An instance of Puzzle.
            letter (string): Letter specified by the user
        
        Returns:
            boolean: Returns if the letter is within the word
        """
        letter = letter.lower()
        for i in range(0, len(self._selected_word)):
            if self._selected_word[i] == letter:
                return True
        return False

    def update_display(self, letter):
        """Updates and adds the letter to the blank spaces of the displayed word.

        Args:
            self (Puzzle): An instance of Puzzle.
            letter (string): Letter specified by the user
        """

        letter = letter.lower()
        for i in range(0, len(self._selected_word)):
            if self._selected_word[i] == letter:
                if i == 0:
                    self._display = letter + self._display[1:]
                elif i == len(self._selected_word):
                    self._display = self._display[:i] + letter
                else:
                    self._display = self._display[:i] + letter + self._display[i+1:] 

    def print_display(self):
        """Prints the letters found and the spaces left

        Args: 
            self (Puzzle): An instance of Puzzzle.
        """
        print(self._display)

    def verify_victory(self):
        """Prints the letters found and the spaces left

        Args: 
            self (Puzzle): An instance of Puzzzle.
        """
        if self._display == self._selected_word:
            return True
        else:
            return False