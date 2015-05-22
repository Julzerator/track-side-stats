"""Track Side Stats."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime
from model import (connect_to_db, db, User, LeagueUser, Team, Player, 
                  TeamPlayer, League, Roster, RosterPlayer, Game,
                  Jam, JamPosition, Action)


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
    # In development

    return render_template('html/index.html')


@app.route('/to_signup')
def to_signup():
    """
    A User requests an account.
    This is not fully realized for demo purposes.
    """
    # In development

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
    # In development

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
    # In development

    flash("Working on implementing this!")

    return redirect("/")


@app.route('/login')
def login():
    """
    Go to the login page if no post information.
    User logs in to the site.
    """
    # In development

    flash("Working on implementing this!")

    return redirect("/")


@app.route('/logout')
def logout():
    """
    User logs out of the site.
    """
    # In development

    flash("Working on implementing this!")

    return redirect("/")


@app.route('/account')
def account_update():
    """
    Go to the account page if no post information.
    Otherwise update the account of current User.
    """
    # In development

    flash("Working on implementing this!")

    return redirect("/")


@app.route('/league', methods=['POST'])
def new_league():
    """ Add a new League. """
    # In development
    
    name = request.form["name_input"]
    affiliation = request.form["affiliation_input"]
    location = request.form["location_input"]
    founded = request.form["founded_input"]

    new_league = League(name=name,
        affiliation=affiliation,
        location=location,
        founded=founded)

    db.session.add(new_league)

    db.session.commit()

    return redirect("/")


@app.route('/league/<int:league_id>')
def league_update(league_id):
    """ League. """
    # In development

    flash("Working on implementing this!")

    return redirect("/")


@app.route('/team', methods=['POST'])
def new_team():
    """ Add a new Team. """
    # In development
    
    league_id = request.form["league_id"]
    name = request.form["name_input"]
    t_type = request.form["t_type_input"]
    founded = request.form["founded_input"]

    new_team = Team(league_id=league_id,
        name=name,
        t_type=t_type,
        founded=founded)

    db.session.add(new_team)

    db.session.commit()

    return redirect("/")


@app.route('/team/<int:team_id>')
def team_update(team_id):
    """ Change an existing Team. """
    # In development

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
    # In development

    flash("Working on implementing this!")

    # Stretch goal

    return redirect("/")


@app.route('/player', methods=['POST'])
def new_player():
    """ Add a new Player. """
    # In development

    name = request.form["name_input"]
    legal_fname = request.form["fname_input"]
    legal_lname = request.form["lname_input"]
    number = request.form["number_input"]
    started = request.form["started_input"]

    # Check to see if there is another player with that
    # exact name / number combo.

    players = db.session.query(Player)
    player_check = players.filter(Player.name == name,
        Player.number == number)

    if player_check.first() == None:
        new_player = Player(name=name,
            legal_fname=legal_fname,
            legal_lname=legal_lname,
            number=number,
            started=started)

        db.session.add(new_player)
        db.session.commit()

    else:
        existing_player = player_check.first()
        # Return that the player already exists
        # Show the player name, number, location, and team (if available)

    team_id = request.form["team_id"]

    if team_id != None:
        newest_player = players.filter(Player.name == name,
        Player.number == number).first()
        teamplayer = TeamPlayer(team_id=team_id,
            player_id=newest_player.player_id)

    return redirect("/")


@app.route('/player_details/<int:player_id>')
def player_details(player_id):
    """ Show an existing Player. """
    # In development
    
    player = Player.query.get(player_id)

    return redirect("/")


@app.route('/player/<int:player_id>')
def player_update(player_id):
    """ Change an existing Player. """
    # In development

    flash("Working on implementing this!")

    return redirect("/")


@app.route('/action', methods=['POST'])
def record_action():
    """ 
    Record actions by Blockers and Jammers.
    """
    # In development

    # Record an action (blocker)
    # o Drive jammer out (and null?)
    # o Knock jammer down (and null?)
    # o Screen allowing your jammer by
    # o Draw cut
    # o Whip
    # o Block assist
    # o Penalty (in queue? question to answer.)
    


    # Record an action (jammer)
    # -- These are coded into the JS
    # o Star pass. UGH 
    # o Award Lead Jammer
    # o Call off a jam (by jammer)
    # o Award points
    # o Lost lead
    # o Not lead first pass
    # o Lap number?
    # o Penalty

    jam_id = session.get("jam_id")
    player_id = session.get("player_id")
    play = session.get("play")
    timestamp = datetime.utcnow()

    points = session["points"]

    action = Action(jam_id=jam_id,
        player_id=player_id,
        play=play,
        timestamp=timestamp)

    # Remove this data from the session:
    db.session.add(action)
    db.session.commit()

    session.pop('play', None)
    session.pop('points', None)

    flash("Working on implementing this!")

    return redirect("/")


@app.route('/jam_start')
def jam_start():
    """ Start a new jam. """
    # In development

    flash("Working on implementing this!")

    return redirect("/")


@app.route('/jam_end/<int:jam_id>')
def jam_end(jam_id):
    """ End jam. (call off or injury) """
    # In development

    flash("Working on implementing this!")

    return redirect("/")

@app.route('/between_jams')
def between_jams():
    """Screen to assign new players to positions."""
    # In development

    return render_template("html/between_jams.html")


@app.route('/to_new_game')
def to_new_game():
    """ Direct user to the game setup screen. """
    # In development

    flash("Working on implementing this!")

    return render_template("html/game.html")


@app.route('/new_game', methods=['POST'])
def game_setup():
    """ Create a new game. """
    # In development

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


@app.route('/add_roster/<int:team_id>/<int:ordinal>')
def add_roster(team_id, ordinal):
    """
    Create a new roster for the game, adding all players from the
    team indicated by the game and assigning whether home or opposing.
    """
    # In development

    game_id = 1 #for testing will be: session["game_id"]
    color = 'Choose'

    # Check to see if the game has an assigned home or away team already
    existing = session.query(Roster).filter_by(game_id = game_id).all()

    print existing

    # If so, delete the related roster/player data and create a new roster.


    # Create the new roster (working)

    # roster = Roster(team_id=team_id,
    #     game_id=game_id,
    #     ordinal=ordinal,
    #     color=color)

    # db.session.add(roster)
    # db.session.commit()

    # roster_team = Team.query.get(roster.team_id)
    # print roster_team.name

    # # Add this roster to session under ordinal number.
    # roster = session.query(Roster).filter(Roster.game_id=game_id, 
    #     Roster.ordinal=ordinal, Roster.team_id=team_id).one()

    # session['team'+ ordinal] = roster.roster_id

    # print roster.roster_id

    # # Get the team
    # teamplayers = session.query(TeamPlayer).filter(
    #     TeamPlayer.team_id=team_id)

    # print team.name

    # # Create the new roster for this game.
    # for player in teamplayers:
    #     rosterplayer = RosterPlayer(roster_id=roster.roster_id,
    #         player_id=teamplayers.player_id)
    #     db.session.add(rosterplayer)

    # db.session.commit()

    # # Print the roster to the screen.
    # if 'team1' in session:



    # return redirect("/")


@app.route('/change_roster')
def change_roster():
    """ Add/Remove Player from Roster. """
    # In development

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
    # In development

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
    # In development
    
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