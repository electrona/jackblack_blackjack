def displaymenu():
    
    print('                 WELCOME TO:                                ')
    print('    ╔══════════════════════════════════════════════════════╗')
    print('    ║     ♠ ♦ ♥ ♣ JACK BLACK - Black Jack game ♣ ♥ ♦ ♠     ║')
    print('    ╚══════════════════════════════════════════════════════╝')
    print('')
    print(" COMMAND MENU")
    print('')
    print("Play - Play Black Jack")
    print("Rules - Show Rules")
    print("Exit - Exit program")


def player_float(i):

    print('     ╔══════════════════════════════════════════════════════╗')
    print('     ║   Please enter the amount of Float                   ║')
    print('     ╚══════════════════════════════════════════════════════╝')

    player_float_amount = int (input("Enter Player " + str(i + 1) + "'s float amount: "))
    print("")
    return player_float_amount


def betting_player(player_float_amount, j):

    print("")
    print('    ╔══════════════════════════════════════════════════════╗')
    print('    ║   Minimum bet amount is $5 to a maximum of $1000     ║')
    print('    ╚══════════════════════════════════════════════════════╝')
    print("")

    bet_amount = int(input("Enter Player " + str(j + 1) + "'s bet amount: "))
    float_remain = player_float_amount - bet_amount
    if bet_amount in range(5, 1000) and bet_amount <= player_float_amount and player_float_amount > 0:
        print("")
        print("Your bet amount is: ", bet_amount)
        print("You have " + str(float_remain) + " chips left")
        return float_remain
    else:
        print("Please enter a valid bet")
        print()


    valid = True
    while valid:
        bet_amount = int(input("Enter Player " + str(j + 1) + "'s bet amount: "))
        float_remain = player_float_amount - bet_amount
        if bet_amount in range(5, 1000) and bet_amount <= player_float_amount and player_float_amount > 0:
            print("")
            print("Your bet amount is: ", bet_amount)
            print("You have " + str(float_remain) + " chips left")
            return float_remain
        else:
            print("Please enter a valid bet")
            print()
            valid = True





def rules_display():


    print('')
    print('    ╔══════════════════════════════════════════════════════╗')
    print('    ║  ♠ ♦ ♥ ♣ JACK BLACK - Black Jack game Rules ♣ ♥ ♦ ♠  ║')
    print('    ╚══════════════════════════════════════════════════════╝')
    print('')
    print('╔══════════════════════════════════════════════════════════════╗')
    print('║                                                              ║')
    print('║1. Up to five players can play per round.                     ║')
    print('║                                                              ║')
    print('║2. Minnumum bet is $5 to a maximum of $1000 per round.        ║')
    print('║                                                              ║')
    print('║3. Dealer will automatically hit on 16 and stand at 17.       ║')
    print('║                                                              ║')
    print('║4. There is no spliting cards or doubling down pairs.         ║')
    print('║                                                              ║')
    print('║5. At the end of each round, cards are reshuffled.            ║')
    print('║                                                              ║')
    print('║6. Player(s) can reload their float if they are out of money  ║')
    print('║   at the end of the round.                                   ║')
    print('║                                                              ║')
    print('║7. For additional game rules please visit Casino NLs website  ║')
    print('║   at: www.CasinoNL.com/Blackjack                             ║')
    print('║                                                              ║')
    print('║8. please play in moderation, VLT games and gambling are      ║')
    print('║   addictive.                                                 ║')
    print('║                                                              ║')
    print('╚══════════════════════════════════════════════════════════════╝')


def main():
    """
    displaymenu()
    


    while True:
        command = input("\nCommand: ")
        if command.lower() == "play":
            bettinginput()
        elif command.lower() == "rules":
            rulesdisplay()
        elif command.lower() == "exit":
            break
    print("Bye!")
    
   
   # rulesdisplay()
   """




if __name__=="__main__":
    main()





