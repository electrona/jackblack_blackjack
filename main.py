import deck
import betting
import dealer

import random as rnd

#use tableHands[] to hold multiple playerHand[]
#use .remove()/.pop() to remove cards from single deck
#add ability to change A to 1 OR 11


#dealing cards (player)
def creatingPlayerHand():
    suits = ["\u2660", "\u2665", "\u2666", "\u2663"]
    cardNumbers = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    handValue = 0
    numberOfCards = 0
    playerHand = [handValue]
    for numberOfCards in range(2):
        h = rnd.randrange(13)
        cardNumber = str(cardNumbers[h])
        j = rnd.randrange(3)
        suit = suits[j]
        playerHand.append(cardNumber)
        playerHand.append(suit)
    return playerHand

#takes face value and assigns a numerical value
def cardValueCalculation(playerHand):
    handValue = 0
    cardValue = 0
    for i in range(1, len(playerHand), 2):
        cardNumber = playerHand[i]
        if cardNumber == "J":
            cardValue = 10
        elif cardNumber == "Q":
            cardValue = 10
        elif cardNumber == "K":
            cardValue = 10
        elif cardNumber == "A":
            cardValue = 11
        elif cardNumber == "2":
            cardValue = 2
        elif cardNumber == "3":
            cardValue = 3
        elif cardNumber == "4":
            cardValue = 4
        elif cardNumber == "5":
            cardValue = 5
        elif cardNumber == "6":
            cardValue = 6
        elif cardNumber == "7":
            cardValue = 7
        elif cardNumber == "8":
            cardValue = 8
        elif cardNumber == "9":
            cardValue = 9
        elif cardNumber == "10":
            cardValue = 10
        handValue = handValue + cardValue
    print("Your hand total is: " + str(handValue))
    print()
    playerHand[0] = handValue
    return playerHand

#the game itself
def playGame(playerHand):
    print()
    #betting function/module
    printHand(playerHand)
    again = True
    while again == True:
        cardValueCalculation(playerHand)
        handValue = playerHand[0]        
        if handValue > 21:
            print("You Bust!")
            break
        elif handValue == 21:
            print("You win!")
            break
        choice = input("Would you like to Hit or Stand (h/s) ")
        if choice.lower() == "h":
            hit(playerHand)
        elif choice.lower() == "s":
            stand()
            break
        else:
            print("Invalid Selection. Please try again.")
        printHand(playerHand)
    print()

#to "hit" for another card
def hit(playerHand):
    print("You request another card")
    suits = ["\u2660", "\u2665", "\u2666", "\u2663"]
    cardNumbers = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    h = rnd.randrange(13)
    cardNumber = str(cardNumbers[h])
    j = rnd.randrange(3)
    suit = suits[j]
    playerHand.append(cardNumber)
    playerHand.append(suit)
    print()

#to stay with your current hand
def stand():
    print("You are content with your current hand")

#prints the players hand in organized manner 
def printHand(playerHand):
    for i in range(1, len(playerHand), 2):
        print("[" + playerHand[i] + playerHand[i+1] + "]")
    print()
    
def main():
    playerHand = creatingPlayerHand()
    playGame(playerHand)
    

if __name__ == "__main__":
    main()

