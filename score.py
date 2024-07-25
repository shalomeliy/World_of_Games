import os
import utils


# This function add points to the DB - Scores.py file, for every user winning
def add_score(difficulty):
    # calculate points of winning
    points_of_winning = (int(difficulty) * 3) + 5

    # check that the file is existed
    if os.path.exists(utils.scores_file_name):
        # Open the file and read the current score
        score_file = open("Scores.txt", 'r')
        current_score = score_file.readline()
        if current_score.isdigit():
            current_score = int(current_score)
        else:
            current_score = 0

        # add the new score to exist score
        new_score = int(current_score) + points_of_winning

        # Write the new score to the file
        score_file = open("Scores.txt", 'w+')
        score_file.write(str(new_score))
        score_file.close()

# example usage
# add_score(2)