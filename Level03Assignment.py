import random

#Game applies in a loop after user has responded with Y
play_again = "y" 
while play_again == "Y" or play_again == "y":

    #Generating random number
    random_num = random.randint(1, 100)
    guess_counter = 0

    #Asking for user's guess
    number_guess = int(input("What number do you think it is? "))

    #Incorrect or invalid guess loop
    while number_guess < 1 or number_guess > 100 or random_num != number_guess:
        if number_guess < 1 or number_guess > 100:
            print("Error, please enter a number between 1 and 100.")
        elif random_num < number_guess:
            print("Lower!")
            guess_counter += 1
        else:
            print("Higher!")
            guess_counter += 1
        number_guess = int(input("What number do you think it is? "))

    #Correct guess results
    if random_num == number_guess:
        guess_counter += 1
        print("Correct!")
        print(f"You got it in {guess_counter} guesses!")

    if random_num == number_guess and guess_counter <= 3:
        print("Amazing!")
    elif random_num == number_guess and guess_counter > 3 and guess_counter <= 5:
        print("Impressive!")
    elif random_num == number_guess and guess_counter > 5 and guess_counter <= 7:
        print("Good job!")
    elif random_num == number_guess and guess_counter > 7 and guess_counter <= 9:
        print("Took a little longer, but you got there!")
    elif random_num == number_guess and guess_counter >= 10:
        print("You need to lock in.")

    #Asking if user would like to play again
    play_again = str(input("Would you like to play again? "))

    #If user would not like to play again
else: 
    print("Goodbye!")