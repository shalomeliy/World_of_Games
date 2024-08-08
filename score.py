import os
import utils


# This function adds points to the DB - Scores.txt file for every user win
def add_score(difficulty):

    # Calculate points of winning
    points_of_winning = (difficulty * 3) + 5

    # Check if the scores file exists
    if os.path.exists(utils.scores_file_name):
        # Open the file and read the current score
        with open(utils.scores_file_name, 'r') as score_file:
            current_score = score_file.readline().strip()

        # Validate if current_score is a digit
        if current_score.isdigit():
            current_score = int(current_score)
        else:
            current_score = 0
    else:
        # If the file does not exist, initialize the score to 0
        current_score = 0

    # Calculate new score
    new_score = current_score + points_of_winning

    # Write the new score to the file
    with open(utils.scores_file_name, 'w') as score_file:
        score_file.write(str(new_score))

# Example usage:
#add_score(3)
