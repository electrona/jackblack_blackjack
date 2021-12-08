#will not be separate module, placed here to not f up main while being worked on


if dealer_hand == player_hand:
    print("Push!")
    chip_stacks += bet_amount

if dealer_hand > player_hand:
    print("Dealer wins :(")
    money += chip_stacks    #this adds to dealersNet csv

if dealer_hand < player_hand:
    print("Player wins!")
    chip_stacks += (2 * bet_amount)    #adds what player bet and their winnings to chip_stacks
    money -= (2 * bet_amount)           #minuses player winnings from dealersNet csv


