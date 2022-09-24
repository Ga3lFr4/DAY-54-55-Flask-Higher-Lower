from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def greet_user():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

winning_num = random.randint(0, 9)

@app.route('/<int:guessed>')
def check_win(guessed):
    if guessed == winning_num:
        return '<h1 style=color:green>You win!</h1>' \
               '<img src="https://media2.giphy.com/media/1jWaJ8RgySqOaPjl45/giphy.gif?cid=ecf05e4740vuazfrnrt7fooxffrjhlqckjbv2hbgv8efi57x&rid=giphy.gif&ct=g"/>'
    elif guessed < winning_num:
        return '<h1 style=color:purple>Too low, try again!</h1>' \
               '<img src="https://media2.giphy.com/media/hWm5wAsxYdl8N2MlFh/giphy.gif?cid=ecf05e47h1of4zbxl6v6d25umokwegbvfecw9zxqbegju3qi&rid=giphy.gif&ct=g"/>'
    else:
        return '<h1 style=color:blue>Too high, try again!</h1>' \
               '<img src="https://media0.giphy.com/media/URoLoCo1s9jm8/giphy.gif?cid=ecf05e47h1of4zbxl6v6d25umokwegbvfecw9zxqbegju3qi&rid=giphy.gif&ct=g"/>'


if __name__ == "__main__" :
    app.run(debug=True)