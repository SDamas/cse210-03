import random

#File that holds the secret words for the game.

#Themes of secret words option
object = ["computer", "box", "chair"]
animal = ["lion", "bear", "eagle"]
color = ["blue", "black", "green"]

def pick(theme):
    """
    Picks a random word for the game theme.

    returns: word = random word from the theme list. 
    """
    word = ""

    if theme.lower() == "object":
        word = random.choice(object)
    elif theme.lower() == "animal":
        word = random.choice(animal)
    elif theme.lower() == "color":
        word = random.choice(color)

    return word