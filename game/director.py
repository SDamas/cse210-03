from game.puzzle import Puzzle
from game.player import Player
from game.skydiver import Skydiver

class Director:
    """
    The role of the director is to hold and run the game's logic structure.

    Attributes:
        puzzle (Puzzle): The game's content.
        player (Player): The game's player.
        skydiver (Skydiver): The player's character.
        is_playing (boolean): Whether or not to keep playing.
    """

    def __init__(self):
        """
        Class' constructor

        Args:
            self (Director): An instance of Director
        """

        self._puzzle = Puzzle()
        self._player = Player()
        self._skydiver = Skydiver()
        self._is_playing = True

    def start_game(self):
        """
        Start and run the loop for the game

        Args:
            self (Director): An instance of Director
        """
        #Print game opening message
        print("Hello, welcome to the Jumper Game!")
        print("How's your luck today?")

        #Player chooses the theme
        theme = input("Choose a theme: ")

        #Generating secret word
        self._puzzle.generate_secret_word(theme)

        while self._is_playing:

            self.display_game_interface()
            self.do_updates()
            self.do_outputs()

    def display_game_interface(self):
        """
        Displays the game interface

        Args:
            self (Director): An instance of Director
        """

        #Displaying the secret word
        secret_word = self._puzzle.display_secret_word()
        print(secret_word)

        #Displaying parachute
        self._skydiver.display_parachute()

    def do_updates(self):
        """
        Do any necessary update in secret word or player's parachute

        Args: 
            self (Director): An instance of Director
        """

        #Getting guess from the player
        self._player.guess()

        #Checking if player's guess is in the secret word
        guess = self._player.get_guess()
        self._puzzle.check_guess(guess) #This line is to update the instance of puzzle in the game.

        guess_in_secret_word = self._puzzle.check_guess(guess) #This line is used for the logic below
        #to see if parachute will be cut or not.

        if not guess_in_secret_word:
            self._skydiver.cut_parachute()

    def do_outputs(self):
        """
        Check if player wins or not

        Args: 
            self (Director): An instance of Director
        """

        #Check if player win
        win = self._puzzle.check_win()
        if win:
            print("Congratulations, you won!")

            self._is_playing = False

        # #Check if player lose
        # lose = self._player.check_life()
        # if lose:
            # print("Looks like your luck is against you today.")

            # self._is_playing = False
