"""Track Side Stats."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime
from model import (connect_to_db, db, User, LeagueUser, Team, Player, 
                  Position, TeamPlayer, League, Roster, RosterPlayer,
                  Game, Jam, JamPosition, Action)


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


    return render_template('html/index.html')


@app.route('/to_signup')
def to_signup():
    """
    A User requests an account.
    This is not fully realized for demo purposes.
    """

    # I want to return their info then
    # email them a link in the final version.
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/signup')
def signup():
    """
    A User requests an account.
    This is not fully realized for demo purposes.
    """

    # I want to return their info then
    # email them a link in the final version.
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/to_login')
def to_login():
    """
    Go to the login page if no post information.
    User logs in to the site.
    """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/login')
def login():
    """
    Go to the login page if no post information.
    User logs in to the site.
    """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/logout')
def logout():
    """
    User logs out of the site.
    """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/account')
def account_update():
    """
    Go to the account page if no post information.
    Otherwise update the account of current User.
    """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/league')
def new_league():
    """ Add a new League. """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/league/<int:league_id>')
def league_update(league_id):
    """ League. """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/team')
def new_team():
    """ Add a new Team. """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/team/<int:team_id>')
def team_update(team_id):
    """ Change an existing Team. """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/load_team')
def load_team():
    """
    Load a csv and add all players to a team.
    If the player exists with the same name and number combo,
    (checking to see if the numbers with letters are checked
        with letters removed.)
    hold onto that players existing id and warn user that
    the player already exists and see if they want to add this
    player... otherwise create the new player.
    """
    flash("Working on implementing this!")

    # Stretch goal

    return redirect("/")


@app.route('/player')
def new_player():
    """ Add a new Player. """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/player/<int:player_id>')
def player_update(player_id):
    """ Change an existing Player. """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/blocker/<int:jam_id>/<int:player_id>')
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
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/jammer/<int:jam_id>/<int:player_id>')
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
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/jam_start')
def jam_start():
    """ Start a new jam. """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/jam_end/<int:jam_id>')
def jam_end(jam_id):
    """ End jam. (call off or injury) """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/to_new_game')
def to_new_game():
    """ Direct user to the game setup screen. """
    flash("Working on implementing this!")

    return render_template("html/game.html")


@app.route('/new_game', methods=['POST'])
def game_setup():
    """ Create a new game. """

    date = request.form["date_input"]
    location = request.form["location_input"]
    event_name = request.form["event_input"]
    g_type = request.form["g_type_input"]
    floor = request.form["floor_input"]

    new_game = Game(date=date,
                    location=location,
                    event_name=event_name,
                    g_type=g_type,
                    floor=floor)

    print new_game

    # db.session.add(new_game)

    # db.session.commit()

    flash("Working on implementing this!")

    return redirect("/to_new_game")


@app.route('/add_roster')
def add_roster():
    """
    Create a new roster for the game, adding all players from the
    team indicated by the game and assigning whether home or opposing.
    """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/change_roster')
def change_roster():
    """ Add/Remove Player from Roster. """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/show_roster')
def show_roster():
    """
    Order roster by Derby Ordering.
    - this is basically ordering by first number
    in the player number, then by the second number
    in the player number, etc... player numbers that
    start with a letter are alphabetical at the end
    of the list.
    """
    flash("Working on implementing this!")

    return redirect("/")


@app.route('/analyze')
def analyze():
    """
    Data analysis:
    o +/- point differential
    o Who are the best together
    o -- point differential as a line
    o 
    """
    flash("Working on implementing this!")

    # Stretch goal

    return redirect("/")


###############################################################
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()