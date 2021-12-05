import csv
import casinodeck
import betting

FILENAME = "dealersNet.csv"

def write_dealersNet(money): #this might have to be in the player module, assigning win/loss to csv
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(money)

def read_dealerNET():
    money = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            money.append(row)
    return money

def displayWinLoss():
    pass #may not need

def shuffle_deck():
    pass #import casinodeck with shuffle function
    casinodeck.new_deck()


def main():
    # display a welcome message
    print("This is the dealer")
    print()

    current_balance = read_dealerNET()
    #displayWinLoss() #may not need

    choice = "y"
    while choice.lower() == "y":
        hand_payout = betting."futurefunction()" #hand_payout would need to be imported
                            #-50          +     -100   = -150
        net_plus_minus = (current_balance + hand_payout)

        print("Dealers Net +/-: " + str(net_plus_minus))
        print()

        # money = []
        # money.append(net_plus_minus)

        choice = input("View balance again? (y/n):")

if __name__ == "__main__":
    main()