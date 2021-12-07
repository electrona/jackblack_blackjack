def bettinginput():
    print('')
    print('    ╔══════════════════════════════════════════════════════╗')
    print('    ║  ♠ ♦ ♥ ♣ JACK BLACK - Black Jack game ♣ ♥ ♦ ♠        ║')
    print('    ╚══════════════════════════════════════════════════════╝')
    
    print("Plese enter the amount of money for your float")
    print("")
    floatamount = int (input("Enter your float amount: "))
    print("")
    print("Minumum bet amount is $5 to a maximum of $1000")
    print("")
    betamount= int (input("Enter your bet amount: "))
    
    floatremain = betamount - floatamount
    
    
    
    if betamount in range(5,1000) and betamount < floatamount and floatamount > 0:
        print("Your bet amount is: ", betamount)
        
    else:
        print("Please enter a valid bet")
        return
        
        
        
        
        
 





def rulesdisplay():

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
    
    
    
    
    bettinginput()
    rulesdisplay()


if __name__=="__main__":
    main()
                  




