import casinodeck as deck
import casinoplayer as player
import betting as bet
import dealer
import random as rnd





# to stay with your current hand
def stand():
    print()
    print("\nYou are content with your current hand")


def create_player_hand(game_deck, player_hand):
    player.hit(game_deck, player_hand)
    player.hit(game_deck, player_hand)


def main():
    player_chip_stacks = []
    game_deck = deck.new_deck()
    player_float_amount = []

    while True:
        number_of_players = int(input("How many Players (1-5): "))  # validation between 1 & 5
        if number_of_players in range(1, 6):
            break
        else:
            print("The maximum number of players is 5. Please try again.")

    for i in range(0, number_of_players):
        chip_stacks = bet.player_float(i)
        player_chip_stacks.append(chip_stacks)
        #player_float_amount.append(0)
    # print(player_chip_stacks)  #test

    play_again = "y"
    while play_again.lower() == "y":
        bet_amount = []
        dealer_hand = dealer.dealers_hand(game_deck)               # not consistent
        dealer_shown_card = dealer_hand[1]                         # stays consistent no matter the dealer hand

        # round of betting before hands are dealt
        for j in range(0, number_of_players):
            player_float_amount = player_chip_stacks[j]
            bet_made = bet.betting_player(player_float_amount, j)
            player_chip_stacks[j] = player_float_amount - bet_made
            bet_amount.append(bet_made)
            bet_made = 0
            # print(bet_amount)               # test
            # print(player_chip_stacks[j])    # test
            print()

        for i in range(0, number_of_players):
            print("===============================")
            print("Player " + str(i + 1) + "'s Turn")
            print()
            player_hand = [0, 0]
            create_player_hand(game_deck, player_hand)
            player.print_hand(player_hand)
            # print("Dealer is showing " + dealer_shown_card)
            if dealer_hand[0] == 21:              #### this function works do not remove
                print("Dealer has blackjack")
                for g in range(2, number_of_players):
                    player_hand[g] = player.card_value_calculation(player_hand)
                    if player_hand[g] == 21:
                        print("player " + str(g+1) + " also has blackjack")
                        # player ties with dealer, gets money back
                    else:
                        print("player " + str(g+1) + " loses")
                        # player loses bet
            while True:
                player.card_value_calculation(player_hand)
                hand_value = player_hand[0]
                if hand_value > 21:
                    print("You Bust!")
                    break
                elif hand_value == 21:
                    stand()
                print("Dealer is showing [??] " + dealer_shown_card)
                choice = input("\nWould you like to Hit or Stand (h/s) ")
                if choice.lower() == "h":
                    player.hit(game_deck, player_hand)
                    print("you hit")
                    print()
                    player.print_hand(player_hand)  #test
                    #print("Dealer is showing " + dealer_shown_card)  # make into dealer.function()
                elif choice.lower() == "s":
                    stand()
                    print(dealer_hand)
                    print("The dealer has a total of " + str(dealer_hand[0]))      # show dealers hand  ## changes every hand
                    # print(dealer_hand[0])  # show dealers hand value  #test
                    print("player " + str(i + 1))
                    # print(bet_amount)                                 #test
                    """
                    bet_made = bet_amount[i]
                    player_hand_value = player_hand[0]
                    dealer_hand_value = dealer_hand[0]
                    print(player_chip_stacks)
                    #chip_stacks = player_chip_stacks[i]
                    print(player_chip_stacks[i])
                    print(chip_stacks)# error on this line when dealing with player 2
                    player_chip_stacks = bet.hand_comparison(dealer_hand_value, player_hand_value, bet_made,
                                                             chip_stacks)
                    # player_chip_stacks[i] = (player_chip_stacks + chips_won_lost)
                    #player_float_amount += player_chip_stacks
                    print("You now have: " + str(chip_stacks) + " chips")
                    """
                    break
                else:
                    print("Invalid Selection. Please try again.")
            #player.print_hand(player_hand)
           # print()
            print(dealer_hand)    # test
            value = dealer_hand[0]
            value = dealer.dealer_plays_hand(value)
            dealer_hand[0] = value
            print(dealer_hand)
            game_deck = deck.new_deck()  # doesnt work

        play_again = input("would you like to play again? (y/n) ")


if __name__ == "__main__":
    main()
