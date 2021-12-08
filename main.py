import casinodeck as deck
import casinoplayer as player
import betting as bet
import dealer
import random as rnd

# need to add:
# validation
# ace evaluation
# compare player vs dealer



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

    while True:
        number_of_players = int(input("How many Players (1-5): "))      # validation between 1 & 5
        if number_of_players in range(1,6):
            break
        else:
            print("The maximum number of players is 5. Please try again.")

    for i in range(0, number_of_players):
        chip_stacks = bet.player_float(i)
        # chip_stacks = int(input("Whats Player " + str(i + 1) + "'s starting chip stack: "))   # validation between 100 & 10000
        player_chip_stacks.append(chip_stacks)
    print(player_chip_stacks)                         ### test


    #player.print_hand(player_hand) #this removed the extra hand from printing
    play_again = "y"
    while play_again.lower() == "y":
        ##########
        bet_amount = []
        ###########
        dealer_hand = dealer.dealers_hand(game_deck)  # show dealers hand
        dealer_shown_card = dealer_hand[1]

        for j in range(0, number_of_players):
            ###################
            player_float_amount = player_chip_stacks[j]
            player_chip_stacks[j] = bet.betting_player(player_float_amount, j)
            bet_made = player_chip_stacks[j]
            player_float_amount = player_float_amount - bet_made
            bet_amount.append(bet_made)
            bet_made = 0
            print(bet_amount)
            print()
            ####################
        for i in range(0, number_of_players):
            print("===============================")
            print("Player " + str(i+1) + "'s Turn")
            print()
            player_hand = [0, 0]
            create_player_hand(game_deck, player_hand)
            player.print_hand(player_hand)
            print("Dealer is showing " + dealer_shown_card)
            again = True
            while again:
                player.card_value_calculation(player_hand)
                # print(player_hand)                              ### test
                hand_value = player_hand[0]
                if hand_value > 21:
                    print("You Bust!")     # no need to show dealers hand
                    break

                #player_float_amount = player_chip_stacks[i]
                #player_chip_stacks[i] = bet.betting_player(player_float_amount, i)
                #print(player_chip_stacks[i])

                choice = input("Would you like to Hit or Stand (h/s) ")
                if choice.lower() == "h":
                    hit(game_deck, player_hand)
                    print("you hit")
                    print()
                    player.print_hand(player_hand)
                    print("Dealer is showing " + dealer_shown_card)           # make into dealer.function()
                elif choice.lower() == "s":
                    stand(player_hand)
                    # print(dealer.dealers_hand(game_deck))
                    dealer_hand = dealer.dealers_hand(game_deck)   # show dealers hand
                    print(dealer_hand[0])  # show dealers hand value
                    #####################
                    print("player " + str(i+1))
                    print(player_chip_stacks[i])
                    bet_made = 0
                    bet_made = bet_amount[i]
                    player_hand_value = player_hand[0]
                    dealer_hand_value = dealer_hand[0]
                    player_chip_stacks = player_chip_stacks[i]   # error on this line when dealing with player 2
                    player_chip_stacks = bet.hand_comparison(dealer_hand_value, player_hand_value, bet_made, player_chip_stacks)
                    player_float_amount = player_float_amount + player_chip_stacks
                    print("You now have: " + str(player_float_amount) + " chips")
                    #####################
                    break
                else:
                    print("Invalid Selection. Please try again.")
            player.print_hand(player_hand)
            print()
            print(dealer_hand)

        play_again = input("would you like to play again? (y/n) ")


if __name__ == "__main__":
    main()
