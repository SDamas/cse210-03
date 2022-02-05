from word import pick

#Class Puzzle that generates secret word, display it and check for win.
class Puzzle:

    def __init__(self):
        """
        Class Constructor
        """
        self._secret_word = ""
        self._secret_word_display = []

    def generate_secret_word(self, theme):
        """
        Generates and return a secret word.

        Args: (self) / theme = player input for the game theme preference
        """
        secret_word = pick(theme)
        self._secret_word = secret_word

        #Adds "_" in the (self) secret_word_display,
        #hiding the real word from the player.
        for letter in secret_word:
            self._secret_word_display += "_"

    def display_secret_word(self):
        """
        Displays secret word.
        """
        print(self._secret_word_display)

    def check_win(self):
        """
        Checks if there is still a "_" in the secret word being displayed
        to the player.
        If not, player won.

        displays: win = Won game message
                or / lose = Lost game message 
        """

        win = "Congratulations! You won."
        lose = "Sorry, you lost."

        if "_" not in "".join(self._secret_word_display):

            print(win)

