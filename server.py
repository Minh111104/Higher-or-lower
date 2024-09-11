from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


def bold(function):
    def wrapper():
        return '<b>' + function + '</b>'
    return wrapper


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@bold
@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_number:
        return '<h1 style="color:red">Too low, try again!</h1>' \
               '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzVic3g1M3Zxa3cydjB5d3lmbWg1NjMwNjh2YTJ5' \
               'MmhxZzhmYTY5NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPGcifQQyazq5yJPO/giphy.webp" width=500>'
    elif guess > random_number:
        return '<h1 style="color:purple">Too high, try again!</h1>' \
               '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTloa2JzcGc3a3p3dDR3bHpwN2Ziamk4YWw3OW1zb' \
               'zBjaGdrOHo3OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7abAHdYvZdBNnGZq/giphy.webp" width=500>'
    else:
        return '<h1 style="color:green">You found me!</h1>' \
               '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExem5nb3pkZzNtZ2g4bW81Zno2bjFmaTg4M2Vldm43b' \
               'mpwcGJvNml2dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/11jKMjB1waSzjG/giphy.webp" width=500>'


if __name__ == "__main__":
    app.run(debug=True)
