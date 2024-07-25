# This flask creates a server and client (web) for the app
from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        with open('scores.txt', 'r') as file:
            score = file.read()
        return f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is:</h1>
                    <div id="score" style="color:green">{score}</div>
                </body>
            </html>
        """
    except Exception as e:
        return f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>ERROR:</h1>
                    <div id="score" style="color:red">{str(utils.bad_return_code)}</div>
                </body>
            </html>
        """


if __name__ == "__main__":
    app.run(debug=True)