def hit(game_deck, hand):
    card_given = game_deck.pop()
    hand.append(card_given)

def intialize_hand(game_deck, player_hand):
    card_given = game_deck.pop()
    player_hand.append(card_given)

def print_hand(player_hand):
    cards = ""
    for i in range(1, len(player_hand)):
        card = str("[" + player_hand[i] +"]")
        cards = cards + card
    print(cards)

def card_value_calculation(player_hand):
    hand_value = 0
    ace_counter = 0
    ace_in_hand = 0
    for i in range(1, len(player_hand)):
        card_number = player_hand[i]
        card_number = card_number[0]
        if card_number == "J":
            card_value = 10
        elif card_number == "Q":
            card_value = 10
        elif card_number == "K":
            card_value = 10
        elif card_number == "1":
            card_value = 10
        elif card_number == "A":
            card_value = 11
            ace_counter += 1
        else:
            card_value = card_number
        hand_value = hand_value + int(card_value)
    if hand_value > 21 and ace_counter > 0:
        hand_value = hand_value - (ace_counter * 10)
    player_hand[0] = hand_value
    return player_hand, hand_value