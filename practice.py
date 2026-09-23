import random
play_again = "Y"
while play_again == "Y" or play_again == "y":
    question_number = 0
    correct_answers = 0
    five_correct_response = ("Perfect score! You're a math wizard!") 
    four_correct_response = ("Awesome job!")
    three_correct_response = ("Not bad, keep practicing!")
    two_correct_response = ("You'll get there!")
    zero_or_one_response = ("Time to review your times tables!")
 
    while question_number <= 4:
        ran_num_1 = random.randint(2,12)
        ran_num_2 = random.randint(2,12)
        solution = int(ran_num_1 * ran_num_2)
        real_question_number = question_number + 1
        solution_guess = int(input(f"Question {real_question_number}: What is {ran_num_1} x {ran_num_2}? "))
        

        if solution != solution_guess:
            print(f"Incorrect. The correct answer was {solution}.")
            question_number += 1

        elif solution == solution_guess:
            print("Correct!")
            correct_answers += 1
            question_number += 1

    print("Results:")
    print(f"You got {correct_answers}/5 correct")

    if correct_answers == 5:
        response = five_correct_response

    elif correct_answers == 4:
        response = four_correct_response

    elif correct_answers == 3:
        response = three_correct_response

    elif correct_answers == 2:
        response = two_correct_response

    else:
        response = zero_or_one_response 

        
    print(f"{response}")

    play_again = str(input("Would you like to play again? (Y/N): "))






else:
    print("Thanks for playing!")
