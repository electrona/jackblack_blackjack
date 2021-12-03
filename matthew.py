import random as rnd

# use tableHands[] to hold multiple playerHand[] for multiplayer capabilities
# use .remove()/.pop() to remove cards from single deck (done dec 1)
# add ability to change A to 1 OR 11 (done Dec 2)

# template arrays to demostrate where the data is
# table_hands = [player1, player2, player3, player4, player5]
# player = [hand_value, chip_stack, card1, card2,...card10]

# The "master" deck that can recreate a new deck at the end of each hand
DECK = ["A\u2660", "2\u2660", "3\u2660", "4\u2660", "5\u2660", "6\u2660", "7\u2660", "8\u2660", "9\u2660", "10\u2660",
        "J\u2660", "Q\u2660", "K\u2660",  # spades
        "A\u2665", "2\u2665", "3\u2665", "4\u2665", "5\u2665", "6\u2665", "7\u2665", "8\u2665", "9\u2665", "10\u2665",
        "J\u2665", "Q\u2665", "K\u2665",  # Hearts
        "A\u2666", "2\u2666", "3\u2666", "4\u2666", "5\u2666", "6\u2666", "7\u2666", "8\u2666", "9\u2666", "10\u2666",
        "J\u2666", "Q\u2666", "K\u2666",  # diamonds
        "A\u2663", "2\u2663", "3\u2663", "4\u2663", "5\u2663", "6\u2663", "7\u2663", "8\u2663", "9\u2663", "10\u2663",
        "J\u2663", "Q\u2663", "K\u2663"]  # clubs

# The deck that is used by the dealer to deal cards to the players
# it allows removal of cards to avoid duplicates
deck_in_play = DECK  # will have to move to be able to reset the deck after each hand


# dealing cards (player)
def creatingPlayerHand():
    hand_value = 0
    chip_stack = 0
    player_hand = [hand_value, chip_stack] # intializes the players hand with hand_value & chip_stack
    for number_of_cards in range(2):
        i = rnd.randrange(51)
        card_number = str(deck_in_play[i]) # sometimes gets out of range error (i think its fixed now)
        deck_in_play.remove(card_number)
        player_hand.append(card_number)
    print(len(deck_in_play)) # checks if cards have been removed from deck
    print(player_hand) # checks to see if player hand is initalized properly
    return player_hand


# takes face value and assigns a numerical value
def cardValueCalculation(player_hand):    # 10 is being picked up as 1 b/c of card_number[0] = 1 for 10
    hand_value = 0                        # use if statement under card_number = card_number[0] to check if [1] = 0 or \
    for i in range(2, len(player_hand)):
        card_number = player_hand[i]
        # to extract 1st character of card string ex "A\u2660" = "A"
        if card_number[1] == "0":   # may need to be cleaned up
            card_number = 10        #
            # print(card_number)    # just a test to make sure the card_number is correct
        else:
            card_number = card_number[0]
        # assigning numerical values to the cards
        if card_number == "J":
            card_value = 10
        elif card_number == "Q":
            card_value = 10
        elif card_number == "K":
            card_value = 10
        elif card_number == "A":
            card_value = 11
        else:
            card_value = int(card_number)
        # This is to change "A" to 11 to 1 if needed
        if card_value == 11 and hand_value >= 20:
            card_value = 1
        hand_value = hand_value + card_value

    print("Your hand total is: " + str(hand_value))
    print()
    player_hand[0] = hand_value
    return player_hand

# add multiplayer capabilities using table_hands.append(player_hand)
# the game itself
def playGame(player_hand):
    print()
    printHand(player_hand)
    again = True
    while again == True:
        # betting function/module
        choice = input("Would you like to Hit or Stand (h/s) ")
        if choice.lower() == "h":
            hit(player_hand)
        elif choice.lower() == "s":
            stand()
            break
        else:
            print("Invalid Selection. Please try again.")
        printHand(player_hand)
        cardValueCalculation(player_hand)
        hand_value = player_hand[0]
        if hand_value > 21:
            print("You Bust!")
            break
        elif hand_value == 21:
            # check dealers cards
            print("You win!")
            break
    print()


# to "hit" for another card
def hit(player_hand):
    print("You request another card")
    i = rnd.randrange(52)
    card_number = str(deck_in_play[i])
    deck_in_play.remove(card_number)
    player_hand.append(card_number)
    print()


# to stay with your current hand
def stand():
    print("You are content with your current hand")
    # check dealers hand


# prints the players hand in organized manner
def printHand(player_hand):
    for i in range(2, len(player_hand)):
        print("[" + player_hand[i] + "]")
    print()


def main():
    player_hand = creatingPlayerHand()
    playGame(player_hand)


if __name__ == "__main__":
    main()