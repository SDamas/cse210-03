import random

#File that holds the secret words for the game.

#Themes of secret words option
object = ["Computer", "Box", "Chair"]
animal = ["Lion", "Bear", "Eagle"]
color = ["Blue", "Black", "Green"]

def pick(theme):
    """
    Picks a random word for the game theme.

    returns: word = random word from the theme list. 
    """
    word = ""

    if theme == object:
        word = random.choice(object)
    elif theme == animal:
        word = random.choice(animal)
    elif theme == color:
        word = random.choice(color)

    return word