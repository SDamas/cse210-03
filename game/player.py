from game.word import pick

class Player:

    def __init__(self):

        self._theme = ""
        self._guess = ""


    def choose_theme(self, theme):

        """
        This will get the theme from the player
        """
        self._theme = pick(theme)

    def guess(self, guess):
        """
        This will allow the player to guess the word
        """
        self._guess = guess

    def get_guess(self):
        """
        This will return the current guess
        """
        guess = self._guess
        return guess