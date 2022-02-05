class Player:

    def __init__(self):

        self._guess = ""
        self._parachute = [" ____",
                         "/____\ ",
                         "\    /",
                          " \  /", 
                          "  O",
                          "/ | \ ", 
                          "/   \ "]

    @property
    def guess(self):

        guess = input("Guess a letter [a-z]: ")
        self._guess = guess

        return self._guess

    @property
    def parachute(self):

        for index, item in enumerate(self._parachute):
            print(self._parachute[index])

        print()
        print("^^^^^^^")

    def cut_parachute(self, part):

        self._parachute.pop(part)