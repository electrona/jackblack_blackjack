import casinodeck as deck
import casinoplayer as player
import betting
import dealer

import random as rnd


# to "hit" for another card
def hit(player_hand):
    print("You request another card")
    suits = ["\u2660", "\u2665", "\u2666", "\u2663"]
    card_numbers = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    h = rnd.randrange(13)
    card_number = str(card_numbers[h])
    j = rnd.randrange(3)
    suit = suits[j]
    player_hand.append(card_number)
    player_hand.append(suit)
    print()


# to stay with your current hand
def stand():
    print("You are content with your current hand")


# the game itself
def play_game(player_hand):
    print()
    # betting function/module
    print_hand(player_hand)
    again = True
    while again:
        card_value_calculation(player_hand)
        hand_value = player_hand[0]
        if hand_value > 21:
            print("You Bust!")
            break
        elif hand_value == 21:
            print("You win!")
            break
        choice = input("Would you like to Hit or Stand (h/s) ")
        if choice.lower() == "h":
            hit(player_hand)
        elif choice.lower() == "s":
            stand()
            break
        else:
            print("Invalid Selection. Please try again.")
        print_hand(player_hand)
    print()


def main():
    game_deck = deck.new_deck()


if __name__ == "__main__":
    main()
