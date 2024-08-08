from guess_game import guess_game
from currency_roulete_game import currency_roulette_game
from memory_game import memory_game
from score import add_score

score = 0

# Game names and descriptions
games = [
    "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
    "2. Guess Game - guess a number and see if you chose like the computer",
    "3. Currency Roulette - try and guess the value of a random amount of USD in ILS"
]
print("\nWelcome to the World of Game!\n")


# This function collect the username
def welcome():

    while True:
        print("What is your first name?")
        user_name = input()
        if user_name.isalpha():
            print(f'Hi {user_name}, and welcome to the World of Games: The Epic Journey\n')
            return user_name
        else:
            print("Invalid input, Please enter a valid first name only\n")


# This function collect the user selected game
def select_game():
    start_flag = True
    while start_flag:
        print('Please select a game number to play')
        for game in games:
            print(game, '\n')
        s_game = input()
        if s_game.isnumeric() and 1 <= int(s_game) <= len(games) + 1:
            return int(s_game)
        else:
            print(f"\nInvalid input. Please select a game number between 1 and {len(games) + 1}.\n")

      



# This function collect the user difficulty level
def select_difficult():
    while True:
        difficulty = input("Please select a difficulty level between 1 (easy) and 5 (professional): ")
        if difficulty.isnumeric() and 1 <= int(difficulty) <= 5:
            return int(difficulty)
        else:
            print("\nInvalid input. Please select a difficulty level between 1 and 5.\n")



# This function start the selected game and stored the winning points in the scores.txt file
def start_play(user_name):
    game = select_game()
    difficulty = select_difficult()
    print(f'Hello {user_name} and welcome to game: {game} selected difficult is: {difficulty}')
   
    if int(game) == 1:
        memory_result = memory_game(int(difficulty))
        add_score(difficulty)
    elif int(game) == 2:
        guess_result = guess_game(difficulty)
        add_score(difficulty)
    elif int(game) == 3:
        roulette_result = currency_roulette_game(difficulty)
        # print(difficulty) #for test
        add_score(difficulty)
    else:
        print("See you next time player!")



# example usage
# user_name = welcome()
# start_play(user_name)
