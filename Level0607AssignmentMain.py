# Import functions
from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won

# Welcome the player
print("Welcome to Wordle!!")

play_again = "Y"

# Outer loop: runs once per game, as long as the player wants to keep playing
while play_again == "Y" or play_again == "y":

    # Reset everything for a new game
    guess_counter = 0
    player_guess = ""
    used_guesses = []

    # Picking secret word using function
    secret_word = choose_word()

    # Inner loop: runs once per guess, until the player wins or uses all 6 tries
    while guess_counter < 6 and has_won(secret_word, player_guess) == False:

        # Get guess function, and remembering old guess
        print(f"Attempt {guess_counter+1} of 6.")
        player_guess = get_guess(used_guesses)
        used_guesses.append(player_guess)

        # Evaluating player's guess
        result= evaluate_guess(secret_word,player_guess)

        # Display guess function shows the guess and its feedback
        display_guess(player_guess,result)

        guess_counter += 1

    # If the player has guess the word or ran out of guesses
    else:
        # Show a win message, or reveal the secret word if they lost
        if has_won(secret_word, player_guess):
            print(f"{player_guess}! You guessed it!!")
        else:
            print(f"Not quite, the word was {secret_word}! Try again!")

        play_again = input("If you would like to play again, press Y!")

# If the player does not want to play again
else:
    print("Goodbye!")
