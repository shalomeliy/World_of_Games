import random
from utils import screen_cleaner

screen_cleaner()


# This function generate a number to guess according to user difficulty
def generate_number(diff):
    return random.randint(1, int(diff))


# This function collect a guessed number from the user
def get_guess_from_user(diff):
    flag = True
    while flag:
        print('\nGuess a number between 1 and ', diff)
        guessed_number = input()
        guessed_number = int(guessed_number)
        if 1 <= int(guessed_number) <= int(diff):
            return guessed_number
        else:
            print('Invalid input')


# This function compare the user answer VS the random number
def compare_results(secret, guessed):
    if secret == guessed:
        return 'True'
    else:
        return 'False'


# This function starts the game and return the result WIN/LOSE
def guess_game(difficulty):
    secret_number = generate_number(difficulty)
    #print(secret_number) #to see the secret number before guessing
    guessed_number = get_guess_from_user(difficulty)
    result = compare_results(secret_number, guessed_number)
    return result

# Example usage:
# guess_game(2)