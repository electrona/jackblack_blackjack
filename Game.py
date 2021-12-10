import betting as bet
import casinoplayer as player
import casinodeck as deck
import dealer as dealer
import csv
houseNet = "houseNet.csv"

def setting_the_table():
    player_chip_stacks = []
    number_of_players = how_many_players()
    creating_chip_float(number_of_players, player_chip_stacks)
    blackjack(player_chip_stacks, number_of_players)

def read_houseNet():
     money = []
     with open(houseNet, newline="") as file:
         reader = csv.reader(file)
         for row in reader:
            money.append(row)
     return money

def write_houseNet(money):
    with open(houseNet, "w", newline="") as file:
         writer = csv.writer(file)
         writer.writerows(money)

def blackjack(player_chip_stacks, number_of_players):
    money = read_houseNet()
    play_again = "y"
    while play_again.lower() == "y":
        game_deck = deck.new_deck()
        bets_made = []
        player_hand = [0]
        table_hands = []
        dealer_hand = dealer.dealers_hand(game_deck)
        dealer_shown_card = dealer_hand[1]
        for i in range(0, number_of_players):
            bets = bet.betting(player_chip_stacks, i)
            bets_made.append(bets)
        print()

        for i in range(0, number_of_players):
            create_player_hand(game_deck, player_hand)
            print("Player " + str(i + 1))
            player.print_hand(player_hand)
            print()
            player.card_value_calculation(player_hand)
            table_hands.append(player_hand)
            player_hand = [0]

        for i in range(0, number_of_players):
            print("===============================")
            print("Player " + str(i + 1) + "'s Turn")
            print()
            player_hand = table_hands[i]
            player.print_hand(player_hand)
            hand_value = player_hand[0]
            print("Player " + str(i + 1) + "'s hand value is: " + str(hand_value))
            player_hand = table_hands[i]
            if dealer_hand[0] == 21 and len(dealer_hand) == 3:
                print("Dealer has blackjack")
                break

            while True:
                hand = table_hands[i]
                player.card_value_calculation(hand)
                hand_value = hand[0]
                if hand_value > 21:
                    print("You Bust!")
                    break
                elif hand_value == 21 and len(hand) == 3:
                    print("Blackjack!")
                    break
                elif hand_value == 21:
                    stand()
                    break
                print("Dealer is showing [??] " + dealer_shown_card)
                choice = input("\nWould you like to Hit or Stand (h/s) ")
                if choice.lower() == "h":
                    player.hit(game_deck, hand)
                    print("you hit")
                    player_hand = hand
                    player.print_hand(player_hand)
                    player.card_value_calculation(hand)
                    print("Your hand value is: " + str(player_hand[0]))
                    print()
                    table_hands[i] = hand
                    player_hand = [0]
                elif choice.lower() == "s":
                    stand()
                    player_hand = [0]
                    break

        dealer.dealer_plays_hand(dealer_hand)
        print()
        print("dealers hand is: ")
        print(dealer_hand)
        print()
        for h in range(0, number_of_players):
            player_hand = table_hands[h]
            player.print_hand(player_hand)
            print("Player " + str(h + 1) + "'s value of " + str(player_hand[0]))
            if dealer_hand[0] > 21:
                dealer_hand[0] = 0
                print("the dealer busts!!")
            if table_hands[h][0] > 21:
                table_hands[h][0] = 0
            if table_hands[h][0] == 21 and len(table_hands[h]) == 3:
                print("Player's Blackjack wins!")
            if table_hands[h][0] > dealer_hand[0]:
                print("Player " + str(h + 1) + " beat the dealer's value of " + str(dealer_hand[0]))
                print("Player wins " + str(2 * bets_made[h]) + " chips!")
                loss = []
                loss.append(bets_made[h])
                money.append(loss)
                write_houseNet(money)
                player_chip_stacks[h] += (2*bets_made[h])            
            elif table_hands[h][0] < dealer_hand[0]:
                print("The dealer's value of " + str(dealer_hand[0]) + " beat Player " + str(h + 1))
                house_take = bets_made[h]
                print("House takes " + str(house_take))
                take = []
                take.append(house_take)
                money.append(take)
                write_houseNet(money)
            elif table_hands[h][0] == dealer_hand[0]:
                print("Player " + str(h + 1) + " Pushes!")
                print("Player bet returned")
                player_chip_stacks[h] += bets_made[h]
            print()
            if player_chip_stacks[h] < 5:
                player_chip_stacks[h] = int(input("You lost your stack! Enter Player " + str(h + 1) + "'s rebuy amount: "))
        play_again = input("Would you like to play again? (y/n) ")
    print("\nThank you for visiting Jack Black's Blackjack casino! Bye!")

def stand():
    print()
    print("\nYou are content with your current hand")

def create_player_hand(game_deck, player_hand):
    player.intialize_hand(game_deck, player_hand)
    player.intialize_hand(game_deck, player_hand)    

def creating_chip_float(number_of_players, player_chip_stacks):
    for i in range(0, number_of_players):
        chip_stack = bet.player_float(i)
        player_chip_stacks.append(chip_stack)

def how_many_players():
    while True:
        number_of_players = int(input("\nHow many Players (1-5): "))  # validation between 1 & 5
        if number_of_players in range(1, 6):
            return number_of_players
            break
        else:
            print("The maximum number of players is 5. Please try again.")