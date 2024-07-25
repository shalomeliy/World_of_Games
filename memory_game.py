import random
import time
from utils import screen_cleaner


# This function generate a sequence of number/s according to difficulty level
def generate_sequence(diff):
    sequence = [random.randint(1, 101) for n in range(diff)]
    print("\nMemorize the sequence:", sequence, '\n')
    time.sleep(0.7)
    screen_cleaner()
    return sequence


# This function collect a sequence of number/s from the user according to difficulty level
def get_list_from_user(diff):
    for i in range (diff):
        user_input = input(f"Guess the {diff} numbers \n").split()
        return user_input


# This function compare the random sequence VS user sequence and return result to memory_game()
def is_list_equal(random_numbers, user_list, result=0):
    screen_cleaner()
    user_list = list(map(int, user_list))
    for i in range(len(random_numbers)):
        for j in range(len(random_numbers)):
            if random_numbers[i] == user_list[j]:
                result += 1
    if result == len(random_numbers):
        user_list = True
        return result, user_list
    else:
        user_list = False
        return result, user_list


# This function starts the game and return the result WIN/LOSE
def memory_game(diff):
    screen_cleaner()
    random_numbers = generate_sequence(diff)
    user_list = get_list_from_user(diff)
    result, equalize = is_list_equal(random_numbers, user_list)
    print('\n\nyou guessed right', result, 'numbers')
    return equalize

# Example usage:
# memory_game(3)