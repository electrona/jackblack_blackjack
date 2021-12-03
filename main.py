import deck as d
import betting
import dealer

import random as rnd


# use tableHands[] to hold multiple playerHand[]
# use .remove()/.pop() to remove cards from single deck
# add ability to change A to 1 OR 11

# takes face value and assigns a numerical value
def card_value_calculation(player_hand):
    hand_value = 0
    card_value = 0
    for i in range(1, len(player_hand), 2):
        card_number = player_hand[i]
        if card_number == "J":
            card_value = 10
        elif card_number == "Q":
            card_value = 10
        elif card_number == "K":
            card_value = 10
        elif card_number == "A":
            card_value = 11
        else:
            card_value = card_number
        hand_value = hand_value + card_value
    print("Your hand total is: " + str(hand_value))
    print()
    player_hand[0] = hand_value
    return player_hand


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


# prints the players hand in organized manner
def print_hand(player_hand):
    for i in range(1, len(player_hand), 2):
        print("[" + player_hand[i] + player_hand[i + 1] + "]")
    print()


def main():
    deck = d.new_deck()


if __name__ == "__main__":
    main()
