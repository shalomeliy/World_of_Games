from currency_converter import CurrencyConverter
import random
from utils import screen_cleaner

# This function generate and save a random number
random_amount = random.randint(1, 100)
flag = True

screen_cleaner()


# This function collect the guessed numbers from the user
def get_guess_from_user():
    while flag:
        print('\nHow much a ' + str(random_amount) + '$ is worth in Shekels ?')
        print('\nYou can write a float number')
        guessed_amount = float(input())
        if isinstance(guessed_amount, (int, float)):
            return round(float(guessed_amount), 2)
        else:
            print('\nplease guess again following the example xxx.xx')


# This function calculate the maximum interval for not mistakes and according to user difficulty
def get_money_interval(diff):
    return 10 - int(diff)


# This function compare the user answer with the correct result and according to user difficulty
def compare_results(diff):
    c = CurrencyConverter()
    dollar_currency = round((c.convert(1, 'USD', 'ILS')),2)
    real_price = dollar_currency * random_amount
    interval = round((real_price + float(diff)), 2)
    return interval


# This function starts the game and return the result WIN/LOSE
def currency_roulette_game(diff):
    guessed_amount = get_guess_from_user()
    mistake = get_money_interval(diff)
    interval = compare_results(diff)
    if interval + mistake > guessed_amount > interval - mistake:
        print('user wins')
        return True
    else:
        print('user loses')
        return False

# Example usage:
# currency_roulette_game(2)