# This script creates a Flask server to serve a web page displaying the game score
from flask import Flask, Response
import os
import utils

app = Flask(__name__)

@app.route("/")
def score_server():
    # Initialize the score variable with a default message
    score = "Score data is not available."

    # Define the path to the scores file
    scores_file = 'scores.txt'
    
    # Check if the 'scores.txt' file exists
    if not os.path.isfile(scores_file):
        # If the file does not exist, create it
        with open(scores_file, 'w') as file:
            file.write("")  # Create an empty file
        score = "No score data available yet."

    # Check if the file is readable and read the score
    if os.access(scores_file, os.R_OK):
        with open(scores_file, 'r') as file:
            score = file.read().strip() or "No score data available."

    # Return HTML content based on the file status
    if score:
        return Response(
            f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is:</h1>
                    <div id="score" style="color:green">{score}</div>
                </body>
            </html>
            """,
            content_type='text/html'
        )
    else:
        return Response(
            f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>ERROR:</h1>
                    <div id="score" style="color:red">Unable to read score data.</div>
                </body>
            </html>
            """,
            content_type='text/html'
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
