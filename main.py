import casinodeck as deck
import casinoplayer as player
import betting
import dealer
import random as rnd


# alternative hit method
def hit(game_deck, player_hand):
    card_given = game_deck.pop()
    player_hand.append(card_given)


# to stay with your current hand
def stand():
    print("You are content with your current hand")


def main():
    player_hand = []
    game_deck = deck.new_deck()
    hit(game_deck, player_hand)
    print(player_hand)

    # print_hand(player_hand)
    # again = True
    # while again:
    #     card_value_calculation(player_hand)
    #     hand_value = player_hand[0]
    #     if hand_value > 21:
    #         print("You Bust!")
    #         break
    #     elif hand_value == 21:
    #         print("You win!")
    #         break
    #     choice = input("Would you like to Hit or Stand (h/s) ")
    #     if choice.lower() == "h":
    #         hit(player_hand)
    #     elif choice.lower() == "s":
    #         stand()
    #         break
    #     else:
    #         print("Invalid Selection. Please try again.")
    #     print_hand(player_hand)
    # print()


if __name__ == "__main__":
    main()
