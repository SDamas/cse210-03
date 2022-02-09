import random

class Puzzle:

    def __init__(self):
        self._secret_word = ""
        self._display_secret_word = ""

    def check_win():
        pass

    def generate_secret_word(self, theme):
        if theme == "Fruit":
            self.words = ["Apple", "Banana", "Blackberry"]
        elif theme == "City":
            self.words = ["Roma", "Paris", "Londres"]
        return self.words
        
    def display_secret_word(self):
        number = random.randint(0,2)
        return self.words[number]

    def check_guess():
        pass
    

