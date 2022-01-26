from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)

app.config['SECRET_KEY'] = "codecodecode"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def gamepage():
    """creates game board"""

   
    board = boggle_game.make_board()

    #store board in session
    session["board"] = board
    return render_template('board.html', board=board)

@app.route('/guess', methods=["POST"])
def handle_guess():
    return redirect('/')

