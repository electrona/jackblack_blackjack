import Game as game
import betting

def main():
    betting.displaymenu()
    while True:
        command = input("Command: ")
        if command.lower() == "play":
            game.setting_the_table()
        elif command.lower() == "rules":
            betting.rules_display()
        elif command.lower() == "exit":
            print("Thank you for visiting Jack Black's Blackjack casino! Bye!")
            break
        else:
            print("Please enter valid input")

if __name__ == "__main__":
    main()