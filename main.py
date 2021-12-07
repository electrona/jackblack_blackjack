import casinodeck as deck
import casinoplayer as player
#import betting
#import dealer
import random as rnd


# alternative hit method
from jackblack_blackjack import casinoplayer


def hit(game_deck, player_hand):
    card_given = game_deck.pop()
    player_hand.append(card_given)
    # #casinoplayer.card_value_calculation(player_hand)
    # #if player_hand == "A" and hand_value <= 11:
    #         hand_value = hand_value + 10



# to stay with your current hand
def stand(player_hand):
    print("You are content with your current hand")

def create_player_hand(game_deck, player_hand):
    hit(game_deck, player_hand)
    hit(game_deck, player_hand)

def main():

    player_hand = [0, 0]                        # player_hand = [hand_value, chip_stack]
    game_deck = deck.new_deck()
    create_player_hand(game_deck, player_hand)
    #print(player_hand) #gets rid of the double zero's
    #player.card_value_calculation(player_hand)  # gets hand_value of hand #this print total 2x
    player.print_hand(player_hand)              # prints hand in organized manner [card][card]

    #player.print_hand(player_hand) #this removed the extra hand from printing
    again = True
    while again:
         player.card_value_calculation(player_hand)
         hand_value = player_hand[0]
         if hand_value > 21:
             print("You Bust!")
             break
         elif hand_value == 21:
             #check to see if dealer == 21
             #if not print
             print("You win!")
             #else print tie
             break
         choice = input("Would you like to Hit or Stand (h/s) ")
         if choice.lower() == "h":
             hit(game_deck, player_hand)
             print("you hit")
             player.print_hand(player_hand)
         elif choice.lower() == "s":
             stand(player_hand)
             # show dealers hand
             break
         else:
             print("Invalid Selection. Please try again.")
    player.print_hand(player_hand)
    print()


if __name__ == "__main__":
    main()
#fuck this shit