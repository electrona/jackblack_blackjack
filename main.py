import casinodeck as deck
import casinoplayer as player
#import betting
#import dealer
import random as rnd

# need to add:
# validation
# ace evaluation



# alternative hit method
#from jackblack_blackjack import casinoplayer


def hit(game_deck, player_hand):
    card_given = game_deck.pop()
    player_hand.append(card_given)
    # #casinoplayer.card_value_calculation(player_hand)
    # #if player_hand == "A" and hand_value <= 11:
    #         hand_value = hand_value + 10



# to stay with your current hand
def stand(player_hand):
    print()
    print("You are content with your current hand")

def create_player_hand(game_deck, player_hand):
    hit(game_deck, player_hand)
    hit(game_deck, player_hand)

def main():
    player_chip_stacks = []
    #player_hand = [0, 0]      # player_hand = [hand_value, chip_stack] # check range function that start @2 if needed
    game_deck = deck.new_deck()
    number_of_players = int(input("How many Players: "))      # validation between 1 & 5
    for i in range(0, number_of_players):
        chip_stacks = int(input("Whats Player " + str(i + 1) + "'s starting chip stack: "))   # validation between 100 & 10000
        player_chip_stacks.append(chip_stacks)
    print(player_chip_stacks)                         ### test


    #player.print_hand(player_hand) #this removed the extra hand from printing
    play_again = "y"
    while play_again.lower() == "y":
        for i in range(0, number_of_players):
            print("===============================")
            print("Player " + str(i+1) + "'s Turn")
            print()
            player_hand = [0, 0]
            create_player_hand(game_deck, player_hand)
            player.print_hand(player_hand)
            again = True
            while again:
                player.card_value_calculation(player_hand)
                # print(player_hand)                              ### test
                hand_value = player_hand[0]
                if hand_value > 21:
                    print("You Bust!")
                    break
                elif hand_value == 21:
                    #check to see if dealer == 21
                    #if not print
                    print("You win!")
                    print("show dealer hand function")
                    #else print tie
                    break
                print("You have " + str(player_chip_stacks[i]) + " chips")        # bet module
                bet_amount = int(input("How much would you like to bet: "))       # bet module # validation to not exceed current chip stack
                print("You bet " + str(bet_amount))                               # bet module
                player_chip_stacks[i] = player_chip_stacks[i] - bet_amount        # bet module
                print("You have " + str(player_chip_stacks[i]) + " chips left.")  # bet module
                print()                                                           # bet module
                choice = input("Would you like to Hit or Stand (h/s) ")
                if choice.lower() == "h":
                    hit(game_deck, player_hand)
                    print("you hit")
                    print()
                    player.print_hand(player_hand)
                elif choice.lower() == "s":
                    stand(player_hand)
                    print("show dealer hand function")           # show dealers hand
                    print("The dealer has: dealer_hand_value")   # show dealers hand value
                    break
                else:
                    print("Invalid Selection. Please try again.")
            # player.print_hand(player_hand)
            print()
        play_again = input("would you like to play again? (y/n) ")


if __name__ == "__main__":
    main()
