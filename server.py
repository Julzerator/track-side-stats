"""Track Side Stats."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime
import controller


app = Flask(__name__)




# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fixed so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """
    Homepage.
    """


    render_template('index.html')


@app.route('/signup')
def signup():
    """
    A User requests an account.
    This is not fully realized for demo purposes.
    """

    return pass # I want to return their info then
                # email them a link in the final version.


@app.route('/login')
def login():
    """
    Go to the login page if no post information.
    User logs in to the site.
    """

    return pass


@app.route('/logout')
def logout():
    """
    User logs out of the site.
    """

    return pass


@app.route('/account')
def account_update():
    """
    Go to the account page if no post information.
    Otherwise update the account of current User.
    """

    return pass


@app.route('/league/<int:league_id>')
def league_update(league_id):
    """ Add a new or change an existing League. """

    return pass


@app.route('/team/<int:team_id>')
def team_update(team_id):
    """ Add a new Team. """

    return pass


@app.route('/blocker/<int:jam_id>/<int:player_id>'):
def blocker_action(jam_id, player_id):
    """ 
    Record an action (blocker)
    o Drive jammer out (and null?)
    o Knock jammer down (and null?)
    o Screen allowing your jammer by
    o Draw cut
    o Whip
    o Block assist
    o Penalty (in queue? question to answer.)
    """

    return pass


@app.route('/jammer/<int:jam_id>/<int:player_id>'):
def jammer_action(jam_id, player_id):
    """
    Record an action (jammer)
    o Star pass. UGH 
    o Award Lead Jammer
    o Call off a jam (by jammer)
    o Award points
    o Lost lead
    o Not lead first pass
    o Lap number?
    o Penalty
    """

    return pass


@app.route('/jam_start'):
def jam_start():
    """ Start a new jam. """

    return pass


@app.route('/jam_end'):
def jam_end():
    """ End jam. (call off or injury) """

    return pass


@app.route('/new_game'):
def game_setup():
    """ Create a new game. """

    return pass


@app.route('/add_roster'):
def add_roster():
    """
    Create a new roster for the game, adding all players from the
    team indicated by the game and assigning whether home or opposing.
    """

    return pass


@app.route('/change_roster'):
def change_roster():
    """ Add/Remove Player from Roster. """

    return pass


@app.route('/show_roster'):
def show_roster():
    """
    Order roster by Derby Ordering.
    - this is basically ordering by first number
    in the player number, then by the second number
    in the player number, etc... player numbers that
    start with a letter are alphabetical at the end
    of the list.
    """


###############################################################
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()