"""class Skydiver:

    def __init__(self):

        self._guess = ""
        self._parachute = [" ____",
                         "/____\ ",
                         "\    /",
                          " \  /", 
                          "  O",
                          "/ | \ ", 
                          "/   \ "]

    def display_parachute(self):

        for index, item in enumerate(self._parachute):
            print(self._parachute[index])

        print()
        print("^^^^^^^")
        

    def cut_parachute(self):

        self._parachute.pop(0)"""


class Skydiver:

    def __init__(self):

        self._parachute = [" ____",
                         "/____\ ",
                         "\    /",
                          " \  /", 
                          "  O",
                          "/ | \ ", 
                          "/   \ "]
        

    def display_skydiver(self):

        print()
        for i in self._parachute:

            print(i)

    def cut_skydiver(self):

        del self._parachute[0]

        # for i in self._parachute:

        #     print(i)
        
    def check_life(self):

        if len(self._parachute) == 3:
            self._parachute[0] = "x"

            return True