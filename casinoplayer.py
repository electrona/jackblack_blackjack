# prints the players hand in organized manner
def print_hand(player_hand):
    for i in range(2, len(player_hand)):
        print(f"[{player_hand[i]}][{player_hand[i + 1]}]")
    print()


# takes face value and assigns a numerical value
def card_value_calculation(player_hand):
    hand_value = 0
    # card_value = 0
    for i in range(2, len(player_hand)):
        card_number = player_hand[i]
        card_number = card_number[0]  # to extract 1st character of card string ex "A\u2660" = A
        if card_number == "J":
            card_value = 10
        elif card_number == "Q":
            card_value = 10
        elif card_number == "K":
            card_value = 10
        elif card_number == 1:
            card_value = 10
        elif card_number == "A":
            card_value = 11
        else:
            card_value = card_number
        hand_value = hand_value + int(card_value)
    print(f"Your hand total is: {hand_value}\n")
    player_hand[0] = hand_value
    return player_hand


def main():
    pass


if __name__ == "__main__":
    main()
