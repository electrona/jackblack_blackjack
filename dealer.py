import csv
import casinodeck
# import betting

FILENAME = "dealersNet.csv"

def write_dealersNet(money):  # this might have to be in the player module, assigning win/loss to csv
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(money)

def read_dealerNET():
    money = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            money.append(row)
    return money

def displayWinLoss():
    pass #may not need


def dealers_hand(deck):
    hand = [0, 0] #hand = [hand_value, chip_stack]
    for i in range(2):
        cards = deck.pop(i)
        hand.append(cards)
    return hand


def display_dealers_hand(hand):
    if len(hand) == 2:
        print("Dealer has [??] &", hand[1])

def value_dealers_hand(hand):
    hand_total = 0
    card_value = 0
    for i in range(len(hand)):
        card_number = hand[i]

# def display_dealers_hand(hand):
#     if len(hand) == 2:
#         print("Dealer has [??] &", hand[1])
#
#
def value_dealers_hand(dealer_hand):
    hand_total = 0
    card_value = 0
    for i in range(2, len(dealer_hand)):
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
    #print("The dealer has a total of ", hand_total)
    #dealers_total_hand = hand_total
    #return dealers_total_hand
    hand_total = hand_total + int(card_value)
    print(f"The dealer has a total of  {hand_total}.")
    dealer_hand[0] = hand_total
    #return hand
#
# def dealer_plays_hand():
#     pass
# #bring in hand total
# #if loop: total <=16 hit
#     #if hit, draw card, add total
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


def dealer_plays_hand():
    pass
#bring in hand total
#if loop: total <=16 hit
    #if hit, draw card, add total
    #elif total >=17
        #hand = total
    #else:
         #stand
         #break

#if loop: total >= 17 stand
        #hand = total
    #else:
         #break

def main():
    # display a welcome message
    print("This is the dealer")
    print()

    deck = casinodeck.new_deck()
    dealers_hand(deck)
    hand = dealers_hand(deck)


    dealers_hand(hand)

    current_balance = read_dealerNET()
    #displayWinLoss() #may not need
"""
    choice = "y"
    while choice.lower() == "y":
        hand_payout = betting."futurefunction()" #hand_payout would need to be imported
                            #-50    +     -100   = -150
        net_plus_minus = (current_balance + hand_payout)

        print("Dealers Net +/-: " + str(net_plus_minus))
        print()

        money = []
        money.append(net_plus_minus)

        choice = input("View balance again? (y/n):")
"""
if __name__ == "__main__":
    main()

