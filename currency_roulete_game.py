from currency_converter import CurrencyConverter
import random
from utils import screen_cleaner

# This function generates a random amount and sets the flag for the game
def initialize_game():
    global random_amount, flag
    random_amount = random.randint(1, 100)
    flag = True
    screen_cleaner()

# This function collects and validates the user's guessed amount
def get_guess_from_user():
    while True:
        try:
            print(f'\nHow much is {random_amount}$ worth in Shekels?')
            print('You can write a float number')
            guessed_amount = float(input().strip())
            if guessed_amount < 0:
                raise ValueError("Amount cannot be negative.")
            return round(guessed_amount, 2)
        except ValueError as e:
            print(f'\nInvalid input: {e}. Please enter a valid float number (e.g., xxx.xx).')

# This function calculates the maximum allowed error interval based on user difficulty
def get_money_interval(diff):
    try:
        difficulty = int(diff)
        if difficulty < 1 or difficulty > 5:
            raise ValueError("Difficulty level must be between 1 and 5.")
        return 10 - difficulty
    except ValueError as e:
        print(f'\nInvalid difficulty level: {e}. Setting interval to 1.')
        return 1

# This function calculates the interval for comparison based on the real and guessed amounts
def compare_results(diff):
    c = CurrencyConverter()
    dollar_currency = round(c.convert(1, 'USD', 'ILS'), 2)
    real_price = dollar_currency * random_amount
    interval = round(real_price + float(diff), 2)
    return interval

# This function starts the game and returns the result (WIN/LOSE)
def currency_roulette_game(diff):
    guessed_amount = get_guess_from_user()
    mistake = get_money_interval(diff)
    interval = compare_results(diff)
    if interval + mistake > guessed_amount > interval - mistake:
        print('User wins!')
        return True
    else:
        print('User loses.')
        return False

# Example usage:
# initialize_game()
# currency_roulette_game('2')
