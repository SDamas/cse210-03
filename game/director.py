from game.word import Word
from game.puzzle import Puzzle
from game.player import Player

class Director:
    """
    The role of the director is to hold the game's logic structure
    """

    def __init__(self):
        """
        Class' constructor

        Attributes: (Self)
        """

        self._word = Word()
        self._puzzle = Puzzle()
        self._player = Player()
        self._is_playing = True

    def start_game(self):
        """
        Start and runs the loop for the game
        """

        while self._is_playing:

            self.get_inputs()
            self.do_updates()
            self.do_inputs()

    def get_inputs(self):

        
