import random

MASTER_DECK = ["AS", "AC", "AH", "AD",
               "2S", "2C", "2H", "2D",
               "3S", "3C", "3H", "3D",
               "4S", "4C", "4H", "4D",
               "5S", "5C", "5H", "5D",
               "6S", "6C", "6H", "6D",
               "7S", "7C", "7H", "7D",
               "8S", "8C", "8H", "8D",
               "9S", "9C", "9H", "9D",
               "10S", "10C", "10H", "10D",
               "JS", "JC", "JH", "JD",
               "QS", "QC", "QH", "QD",
               "KS", "KC", "KH", "KD", ]


# copy master deck so cards can be removed and deck reset
def new_deck():
    deck = MASTER_DECK
    random.shuffle(deck)
    return deck

