# Importing necessary functions from the 'app' module
from app import start_play, welcome

# Collect the user's first name using the welcome function
user_name = welcome()

# Start a selected game with choosing difficulty while pass the user name to the start_play function
start_play(user_name)
