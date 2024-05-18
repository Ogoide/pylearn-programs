from random import randint

# generate a number for the computer and set the number of player guesses to 1
computer_number = randint(1, 20)
guesses = 1
print("I am thinking of a number between 1 and 20.")

while True:
    # ask the player for a guess, as long as they don't win
    guess = input("Take a guess.\n")
    if guess.strip().isnumeric():
        num_guess = int(guess.strip())
        # win condition
        if num_guess == computer_number:
            print(f"Good job! You guessed my number in {guesses} guesses!")
            break
        # give hints to the player and add their guess number
        elif num_guess < computer_number:
            print("Your guess is too low!")
            guesses += 1
        else:
            print("Your guess is too high!")
            guesses += 1
    else:
        # incase the player enters something other than an int value
        print("Please take a NUMERICAL guess!")
    if guesses > 6:
        # the player loses if they take too many guesses
        print(f"I'm sorry... My number was {computer_number}.")
        break