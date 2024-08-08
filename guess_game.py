import random
from utils import screen_cleaner

# Initialize the game environment
screen_cleaner()


# This function generates a random number to guess according to user difficulty
def generate_number(diff):
    max_value = int(diff)
    if max_value > 0:
        return random.randint(1, max_value)
    else:
        print("Difficulty must be a positive integer. Using default max value of 5.")
        return random.randint(1, max_value)


# This function collects a guessed number from the user with validation
def get_guess_from_user(diff):
    max_value = int(diff)
    while True:
        print(f'\nGuess a number between 1 and {max_value}:')
        guessed_number_str = input().strip()
        if guessed_number_str.isdigit():
            guessed_number = int(guessed_number_str)
            if 1 <= guessed_number <= max_value:
                return guessed_number
            else:
                print(f'Invalid input. Please enter a number between 1 and {max_value}.')
        else:
            print('Invalid input. Please enter a valid integer.')


# This function compares the user’s guess to the secret number
def compare_results(secret, guessed):
    return 'True' if secret == guessed else 'False'


# This function starts the game and returns the result (WIN/LOSE)
def guess_game(difficulty):
    max_value = int(difficulty)
    if max_value <= 0:
        print("Difficulty must be a positive integer. Game cannot start.")
        return 'Error'

    secret_number = generate_number(difficulty)
    # print(secret_number) # Uncomment to see the secret number before guessing
    guessed_number = get_guess_from_user(difficulty)
    result = compare_results(secret_number, guessed_number)
    print('You win!' if result == 'True' else 'You lose.')
    return result

# Example usage:
#guess_game(5)
