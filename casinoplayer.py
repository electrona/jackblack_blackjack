# prints the players hand in organized manner
def print_hand(player_hand):
    for i in range(1, len(player_hand), 2):
        print("[" + player_hand[i] + player_hand[i + 1] + "]")
    print()


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


def main():
    pass


if __name__ == "__main__":
    main()
