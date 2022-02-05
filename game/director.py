from game.word import Word
from game.puzzle import Puzzle
from game.player import Player
from game.skydiver import Skydiver

class Director:
    """
    The role of the director is to hold the game's logic structure
    """

    def __init__(self):
        """
        Class' constructor

        Attributes: (Self)
        """

        self._puzzle = Puzzle()
        #should word really be a class?
        self._word = Word()
        self._secret_word = self._word.pick(self._puzzle.generate_secret_word())
        self._player = Player()
        self._skydiver = Skydiver()
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

        #Displaying the secret word
        secret_word = self._secret_word.display_secret_word()
        print(secret_word)

        #Displaying parachute
        self._skydiver.display_parachute()





        
