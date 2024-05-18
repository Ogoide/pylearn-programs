from random import randint

print("ROCK, PAPER, SCISSORS!")
action_list = ["ROCK", "PAPER", "SCISSORS"]
wins = 0
losses = 0
draws = 0
games = 1

while True:
    # print the game statistics and set the computer's action
    print(f"Game {games}:\n{wins} wins. {losses} losses. {draws} draws.")
    computer_action = action_list[randint(0, 2)]

    # ask for player input
    player_action = input("Choose your action:\n[R]ock\n[P]aper\n[S]cissors\n[Q]uit\n")
    # iterate over player input, correlating with the computer's action
    if player_action.strip().lower() == "r":
        print("ROCK versus...")
        if computer_action == "PAPER":
            print("...PAPER")
            print("You loose!\n")
            losses += 1
            games += 1
        elif computer_action == "ROCK":
            print("...ROCK")
            print("It's a draw!\n")
            draws += 1
            games += 1
        elif computer_action == "SCISSORS":
            print("...SCISSORS")
            print("You win!\n")
            wins += 1
            games += 1
    elif player_action.strip().lower() == "p":
        print("PAPER versus...")
        if computer_action == "PAPER":
            print("...PAPER")
            print("It's a draw!\n")
            draws += 1
            games += 1
        elif computer_action == "ROCK":
            print("...ROCK")
            print("You win!\n")
            wins += 1
            games += 1
        elif computer_action == "SCISSORS":
            print("...SCISSORS")
            print("You loose!\n")
            losses += 1
            games += 1
    elif player_action.strip().lower() == "s":
        print("SCISSORS versus...")
        if computer_action == "PAPER":
            print("...PAPER")
            print("You win!\n")
            wins += 1
            games += 1
        elif computer_action == "ROCK":
            print("...ROCK")
            print("You loose!\n")
            losses += 1
            games += 1
        elif computer_action == "SCISSORS":
            print("...SCISSORS")
            print("It's a draw!\n")
            draws += 1
            games += 1
    elif player_action.strip().lower() == "q":
        print(
            f"You quit after playing {games - 1} games, with {wins} wins, {losses} losses and {draws} draws.")
        print("See you next time!")
        break
    else:
        print("Sorry, I couldn't understand your choice!\n")
