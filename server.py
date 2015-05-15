"""Track Side Stats."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, LeagueUser, Team, Player,
    Position, TeamPlayer, League, PersonPosition, Roster, RosterPlayer,
    Game, Jam, JamPosition, Action
from datetime import datetime


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


@app.route('/league')


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()