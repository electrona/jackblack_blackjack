import csv
import casinodeck as casino
import casinodeck

def dealers_hand(game_deck):
    hand = [0]
    for i in range(2):
        cards = game_deck.pop()
        hand.append(cards)
    hand_value = 0
    ace_counter = 0
    for i in range(1, len(hand)):
        card_number = hand[i]
        card_number = card_number[0]
        if card_number == "J":
            card_value = 10
        elif card_number == "1":
            card_value = 10
        elif card_number == "Q":
            card_value = 10
        elif card_number == "K":
            card_value = 10
        elif card_number == "A":
            card_value = 11
            ace_counter += 1
        else:
            card_value = card_number
        hand_value = hand_value + int(card_value)
    if hand_value > 21 and ace_counter > 0:
        hand_value = hand_value - (ace_counter * 10)    
    hand[0] = hand_value
    return hand

def value_dealers_hand(dealer_hand):
    hand_total = 0
    ace_counter = 0
    for i in range(1, len(dealer_hand)):
        card_number = dealer_hand[i]
        card_number = card_number[0]
        if card_number == "J":
            card_value = 10
        elif card_number == "1":
            card_value = 10
        elif card_number == "Q":
            card_value = 10
        elif card_number == "K":
            card_value = 10
        elif card_number == "A":
            card_value = 11
        else:
            card_value = card_number
        hand_total = hand_total + int(card_value)
    if hand_total > 21 and ace_counter > 0:
        hand_total = hand_total - (ace_counter * 10)
    dealer_hand[0] = hand_total

def dealer_plays_hand(dealer_hand):
    game_deck = casinodeck.new_deck()
    while True:
        value = dealer_hand[0]
        if value <= 16:
            print()
            print("dealer hits")
            hit(game_deck, dealer_hand)
            value_dealers_hand(dealer_hand)
        elif value > 21:
            print("dealer busts")
            break
        else:
            break
    dealer_hand[0] = value
    return value

def hit(game_deck, dealer_hand):
    card_given = game_deck.pop()
    dealer_hand.append(card_given)