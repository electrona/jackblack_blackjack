import csv
import casinodeck as casino

FILENAME = "dealersNet.csv"

# def write_dealersNet(money):  # this might have to be in the player module, assigning win/loss to csv
#     with open(FILENAME, "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(money)
#
# def read_dealerNET():
#     money = []
#     with open(FILENAME, newline="") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             money.append(row)
#     return money

def displayWinLoss():
    pass #may not need


def dealers_hand(game_deck):
    hand = [0] #hand = [hand_value, chip_stack]
    for i in range(2):
        cards = game_deck.pop()
        hand.append(cards)
    return hand


def value_dealers_hand(dealer_hand):
    hand_total = 0
    card_value = 0
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
    print(f"The dealer has a total of  {hand_total}.")
    dealer_hand[0] = hand_total


# def dealer_plays_hand(dealer_hand):
#     pass
# # #bring in hand total
#     if dealer_hand <=16:  #hit

#  #if hit, draw card, add total
#     #elif total >=17
#         #hand = total
#     #else:
#          #stand
#          #break
#
# #if loop: total >= 17 stand
#         #hand = total
#     #else:
#          #break



