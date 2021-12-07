import casinodeck as deck
import casinoplayer as player
#import betting
#import dealer
import random as rnd


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
    print("You are content with your current hand")

def create_player_hand(game_deck, player_hand):
    hit(game_deck, player_hand)
    hit(game_deck, player_hand)

def main():
    player_chip_stacks = []
    #player_hand = [0, 0]                        # player_hand = [hand_value, chip_stack]
    game_deck = deck.new_deck()
    number_of_players = int(input("How many Players: "))
    for i in range(0, number_of_players):
        chip_stacks = int(input("Whats your starting chip stack: "))
        player_chip_stacks.append(chip_stacks)
    print(player_chip_stacks)                         ### test
    #create_player_hand(game_deck, player_hand)
    #print(player_hand) #gets rid of the double zero's
    #player.card_value_calculation(player_hand)  # gets hand_value of hand #this print total 2x
                  # prints hand in organized manner [card][card]



    #player.print_hand(player_hand) #this removed the extra hand from printing
    for i in range(0, number_of_players):   # want it to loop only when player finishes their hand
        print("===============================")
        print("Player " + str(i+1) + "'s Turn")
        player_hand = [0, 0]
        create_player_hand(game_deck, player_hand)
        player.print_hand(player_hand)
        again = True
        while again:
            player.card_value_calculation(player_hand)
            print(player_hand)                              ### test
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
            print("You have " + str(player_chip_stacks[i]) + " chips")
            bet_amount = int(input("How much would you like to bet: "))
            print("You bet " + str(bet_amount))
            print("You have " + str(player_chip_stacks[i] - bet_amount) + " chips left.")
            print()
            choice = input("Would you like to Hit or Stand (h/s) ")
            if choice.lower() == "h":
                hit(game_deck, player_hand)
                print("you hit")
                player.print_hand(player_hand)
            elif choice.lower() == "s":
                stand(player_hand)
                print("show dealer hand function")   # show dealers hand
                break
            else:
                print("Invalid Selection. Please try again.")
        player.print_hand(player_hand)
        print()


if __name__ == "__main__":
    main()
