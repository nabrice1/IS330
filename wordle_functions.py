
import random


# List of possible secret words (all 5 letters, no repeated letters)
WORDS = [
    "brave", "crane", "dance", "flame", "grape", "house", "joker", "knife", "lemon", "mango",
    "night", "ocean", "piano", "stone", "tiger", "whale", "yacht", "zebra", "plant", "smile",
    "train", "cloud", "unity", "input", "blame", "chart", "drive", "frost", "ghost", "horse",
    "juice", "laser", "mouse", "noble", "orbit", "pride", "quiet", "roast", "shark", "storm",
    "table", "vapor", "waltz", "young", "zesty", "badge", "cabin", "depth", "eight", "fable",
    "giant", "hotel", "irony", "jumpy", "knelt", "lunch", "magic", "nerdy", "olive", "paint",
    "quart", "ranch", "scout", "thumb", "ulcer", "voice", "world", "yeast", "bread", "climb",
    "dwarf", "fight", "globe", "heart", "judge", "light", "march", "north", "prism", "rusty",
    "sword", "trick", "upset", "vocal", "wrist", "spicy", "blunt", "crisp", "dream", "flock",
    "grind", "candy", "flute", "mirth", "plumb", "shove", "wheat", "cramp", "glory", "fresh",
]


# Picks a random secret word from the WORDS list
def choose_word():
    return random.choice(WORDS)


# Asks the player for a guess and verifies it
def get_guess(used_guesses):
    player_guess = input("What do you think the word is? ").lower()

    
    while len(player_guess) != 5 or player_guess in used_guesses:
        if len(player_guess) != 5:
            print("Your guess must be exactly 5 letters.")
        else:
            print("You already guessed that word. Try a different one.")

        player_guess = input("What do you think the word is? ").lower()

    return player_guess


# Compares the guess to the secret word one letter at a time and builds feedback:
def evaluate_guess(secret_word, player_guess):
    result = ""

    for i in range(len(secret_word)):
        if player_guess[i] == secret_word[i]:
            result = result + "G"
        elif player_guess[i] in secret_word:
            result = result + "Y"
        else:
            result = result + "-"

    return result


# Prints the player's guess with its feedback underneath
def display_guess(player_guess, feedback):
    print("Guess: " + player_guess)
    print("Feedback:   " + feedback)


# Returns True if the guess matches the secret word, otherwise False
def has_won(secret_word, player_guess):
    return player_guess == secret_word
