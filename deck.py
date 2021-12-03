MASTER_DECK = ["A\u2260", "A\u2263", "A\u2265", "A\u2266",
               "2\u2260", "2\u2263", "2\u2265", "2\u2266",
               "3\u2260", "3\u2263", "3\u2265", "3\u2266",
               "4\u2260", "4\u2263", "4\u2265", "4\u2266",
               "5\u2260", "5\u2263", "5\u2265", "5\u2266",
               "6\u2260", "6\u2263", "6\u2265", "6\u2266",
               "7\u2260", "7\u2263", "7\u2265", "7\u2266",
               "8\u2260", "8\u2263", "8\u2265", "8\u2266",
               "9\u2260", "9\u2263", "9\u2265", "9\u2266",
               "10\u2260", "10\u2263", "10\u2265", "10\u2266",
               "J\u2260", "J\u2263", "J\u2265", "J\u2266",
               "Q\u2260", "Q\u2263", "Q\u2265", "Q\u2266",
               "K\u2260", "K\u2263", "K\u2265", "K\u2266", ]
#               Spade      Club       Heart      Diamond

# copy master deck so cards can be removed and deck reset
deck_in_play = MASTER_DECK


# dealing cards (player)
def creating_player_hand():
    hand_value = 0
    chip_stack = 0
    player_hand = [hand_value, chip_stack]  # intializes the players hand with hand_value & chip_stack
    for number_of_cards in range(2):
        i = rnd.randrange(51)
        card_number = str(deck_in_play[i])  # sometimes gets out of range error (i think its fixed now)
        deck_in_play.remove(card_number)
        player_hand.append(card_number)
    print(len(deck_in_play))  # checks if cards have been removed from deck
    print(player_hand)  # checks to see if player hand is initalized properly
    return player_hand
