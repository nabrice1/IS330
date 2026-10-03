import random

#get player choice function
def get_player_choice(): 
    choice = input ("Enter rock, paper, or scissors: ")
    choice = choice.lower()
    while choice not in ("rock", "paper", "scissors"):
        print(f"Sorry {choice} is not a valid choice. Please try again.")
        choice = (input ("Enter rock, paper, or scissors: ")).lower()

    return choice

#determine winner function
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        match_result = "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        match_result = "win"
    else:
        match_result = "loss"

    return match_result

#Initial welcome, while loops, and starting values
play_again = "Y"
print("Welcome to Rock Paper Scissors!")
while play_again == "Y" or play_again == "y":
    rounds_played = 0
    win_count = 0
    lose_count = 0
    rounds_wanted = int(input("How many rounds would you like to play? "))
    while rounds_wanted % 2 == 0:
        rounds_wanted = int(input("Sorry, the number must be an odd number. Please try again: "))

    while rounds_played < rounds_wanted:

#getting payer and computer guesses
        player_choice = get_player_choice()

        computer_options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(computer_options)
        print(f"The computer chose {computer_choice}.")

#determining winner and printing result
        match_result = determine_winner(player_choice, computer_choice)
        if match_result == "win" or match_result == "loss":
            rounds_played += 1

#number of games won and lost if statements
        if match_result == "win":
            win_count += 1
            print("You won!")
        elif match_result == "loss":
            lose_count += 1
            print("You lost!")
        else:
            print("Tie! Play again.")

#overall winner calculator 
    if win_count > lose_count:
        overall_result = "You win!"
    else: 
        overall_result = "You lose!"

#Printing results and asking if user would like to play again
    print(f"Final score - You: {win_count} | Computer: {lose_count}")
    print(overall_result)
    print("Thanks for playing!")
    play_again = input("If you would like to play again press Y! ")

else:
    print("Goodbye!")