import random
import time
from utils import screen_cleaner


# This function generates a sequence of numbers according to the difficulty level
def generate_sequence(diff):
    # Ensure difficulty level is a positive integer
    if diff <= 0:
        raise ValueError("Difficulty level must be a positive integer.")

    sequence = [random.randint(1, 101) for _ in range(diff)]
    print("\nMemorize the sequence:", sequence, '\n')
    time.sleep(0.7)
    screen_cleaner()
    return sequence


# This function collects a sequence of numbers from the user according to the difficulty level
def get_list_from_user(diff):
    user_input = []
    print(f"Guess the {diff} numbers (separated by spaces):")
    input_str = input().strip()
    user_input = input_str.split()

    # Validate the user input
    if len(user_input) != diff:
        print(f"Invalid input. You must enter exactly {diff} numbers.")
        return get_list_from_user(diff)  # Prompt user to try again

    # Convert input to integers and validate
    try:
        user_input = list(map(int, user_input))
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return get_list_from_user(diff)  # Prompt user to try again

    return user_input


# This function compares the random sequence with the user sequence and returns the result
def is_list_equal(random_numbers, user_list):
    screen_cleaner()
    # Validate input lists
    if not all(isinstance(num, int) for num in user_list):
        raise ValueError("User list contains non-integer values.")

    correct_count = sum(1 for num in user_list if num in random_numbers)
    is_correct = (correct_count == len(random_numbers))

    return correct_count, is_correct


# This function starts the game and returns the result WIN/LOSE
def memory_game(diff):
    screen_cleaner()

    # Validate difficulty level
    if diff <= 0:
        raise ValueError("Difficulty level must be a positive integer.")

    random_numbers = generate_sequence(diff)

    user_list = get_list_from_user(diff)
    result, is_correct = is_list_equal(random_numbers, user_list)

    print('\nYou guessed', result, 'number/s correctly.')
    return is_correct

# Example usage:
#memory_game(3)
