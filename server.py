"""Track Side Stats."""

from jinja2 import StrictUndefined
from flask import (Flask, render_template, redirect, request, flash, 
                  session, jsonify)
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


@app.route('/new_league', methods=['GET', 'POST'])
def new_league():
    """ Add a new League. """
    # In testing
    if request.method == 'POST':
        name = request.form["name_input"]
        affiliation = request.form["affiliation_input"]
        location = request.form["location_input"]
        founded = request.form["founded_input"]

        existing = League.query.filter(League.name == name,
            League.affiliation == affiliation,
            League.location == location).first()

        if existing:
            message = "This league is already here: <a href='/league/%d'>/%s</a>!" % (
            existing.league_id, existing.name)

            flash(message)
            
            return redirect("/leagues")

        else:

            new_league = League(name=name,
                affiliation=affiliation,
                location=location,
                founded=founded)

            db.session.add(new_league)
            db.session.commit()

            message = "Thank you for adding <a href='/league/%d'>/%s</a>!" % (
                new_league.league_id, new_league.name)
            flash(message)

            return redirect("/leagues")

    else:
        return render_template("/league.html")


@app.route('/league/<int:league_id>')
def league_details(league_id):
    """ Displays the details of a League. """
    # In testing
    
    league = League.query.filter_by(league_id = league_id).first_or_404()

    league_teams = Team.query.filter_by(league_id = league_id).all()

    league_players = []

    for team in league_teams:
        league_players.extend(team.players)

    return render_template("league_details.html", league=league,
        league_teams = league_teams, league_players = league_players)


@app.route('/leagues')
def league_list():
    """Displaying a list of all leagues"""
    # In testing

    leagues = League.query.all()

    return render_template("league_list.html", leagues=leagues)


@app.route('/new_team', methods=['GET', 'POST'])
def new_team():
    """ Add a new Team. """
    # In testing
    if request.method == 'POST':
        name = request.form["name_input"]
        t_type = request.form["t_type_input"]
        founded = request.form["founded_input"]

        existing = Team.query.filter(Team.name == name,
            Team.t_type == t_type).first()

        if existing:
            message = "This team is already here: <a href='/team/%d'>/%s</a>!" % (
            existing.team_id, existing.name)

            flash(message)
            
            return redirect("/teams")

        else:

            new_team = Team(name=name,
                t_type=t_type,
                founded=founded)

            db.session.add(new_team)
            db.session.commit()

            message = "Thank you for adding <a href='/team/%d'>/%s</a>!" % (
                new_team.team_id, new_team.name)
            flash(message)

            return redirect("/teams")

    else:
        return render_template("/team.html")


@app.route('/team/<int:team_id>')
def team_details(team_id):
    """ Displays the details of a Team. """
    # In testing
    
    team = Team.query.filter_by(team_id = team_id).first_or_404()

    team_players = team.players

    return render_template("team_details.html", team=team,
        team_players = team_players)


@app.route('/teams')
def team_list():
    """Displaying a list of all teams"""
    # In testing

    teams = Team.query.all()

    return render_template("team_list.html", teams=teams)


@app.route('/search_teams')
def search_teams():
    """Search the teams to return a list of teams."""
    # In development

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


@app.route('/new_player', methods=['GET', 'POST'])
def new_player():
    """ Add a new Player. """
    # In development

    if request.method == 'POST':
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

        # team_id = request.form["team_id"]

        # if team_id != None:
        #     newest_player = players.filter(Player.name == name,
        #     Player.number == number).first()
        #     teamplayer = TeamPlayer(team_id=team_id,
        #         player_id=newest_player.player_id)

        return redirect("/")

    else:
        return render_template("/player.html")


@app.route('/player_details/<int:player_id>')
def player_details(player_id):
    """ Show an existing Player. """
    # In development
    
    player = Player.query.get_or_404(player_id)

    return redirect("/")


@app.route('/player/<int:player_id>')
def player_update(player_id):
    """ Change an existing Player. """
    # In development

    flash("Working on implementing this!")

    return redirect("/")


@app.route('/search_players')
def search_players():
    """Search the players to return a list of players."""
    # In development

    return redirect("/")


@app.route('/to_new_game')
def to_new_game():
    """ Direct user to the game setup screen. """
    # In development

    flash("Working on implementing this!")

    return render_template("html/game_setup.html")


@app.route('/new_game', methods=['GET', 'POST'])
def game_setup():
    """ Create a new game. """
    # In development

    game = session.get('game')

    if not game:
        session['game'] = 'new'

    if request.method == 'POST':
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

        db.session.add(new_game)
        db.session.commit()

        session['game'] = {
                           'game_id' : new_game.game_id,
                           'date' : new_game.date.isoformat(),
                           'location' : new_game.location,
                           'event_name' : new_game.event_name,
                           'g_type' : new_game.g_type,
                           'floor' : new_game.floor 
        }

        # Create Home Roster:
        home_team_id = request.form["home_team"]
        home_color = request.form["home_color_input"]
        home = add_roster(new_game.game_id, home_color, home_team_id, 1)
        hometeam = Team.query.get(home_team_id)

        session['home_team'] = {
                                'team_id' : home_team_id,
                                'team_name' : hometeam.name,
                                'roster_id' : home.roster_id
        }

        # Create Away Roster:
        away_team_id = request.form["away_team"]
        away_color = request.form["away_color_input"]
        away = add_roster(new_game.game_id, away_color, away_team_id, 2)
        awayteam = Team.query.get(away_team_id)

        session['away_team'] = {
                                'team_id' : away_team_id,
                                'team_name' : awayteam.name,
                                'roster_id' : away.roster_id
        }

        flash("Game Created!")

        return render_template("html/game.html", home=home, away=away)

    else:
        teams = Team.query.all()
        return render_template("html/game.html", teams=teams)


def add_roster(game_id, color, team_id, ordinal):
    """
    Create a new roster for the game, adding all players from the
    team indicated by the game and assigning whether home or opposing.
    """
    # In development

    # Create the new roster.
    new_roster = Roster(team_id=team_id,
        game_id=game_id,
        ordinal=ordinal,
        color=color)

    db.session.add(new_roster)
    db.session.commit()

    # Get the team
    teamplayers = db.session.query(TeamPlayer).filter(
        TeamPlayer.team_id == team_id).all()

    print teamplayers

    # Add the players to the roster.
    for player in teamplayers:
        rosterplayer = RosterPlayer(
            roster_id=new_roster.roster_id,
            player_id=player.player_id)
        db.session.add(rosterplayer)
    db.session.commit()

    rosterplayers = db.session.query(Player.number, Player.name,
        Player.player_id, RosterPlayer.rospla_id).join(RosterPlayer).filter(
        RosterPlayer.roster_id == new_roster.roster_id).order_by(Player.name)

    return rosterplayers


@app.route('/change_roster/<change_type>')
def change_roster(change_type):
    """ Add/Remove Player from Roster. """
    # In development
    # Use AJAX to update just this part

    if change_type == 'search':
        players = Player.query.all()

    elif change_type == 'add':
        # Get the selected player_id, roster_id and add
        # to RosterPlayer.

    elif change_type == 'remove':
        # Get the selected rospla_id and remove from db.

    return redirect("/")


@app.route('/show_roster/<roster_id>/<ordered_by>')
def show_roster(roster_id, ordered_by):
    """
    Order roster by Derby Ordering.
    - this is basically ordering by first number
    in the player number, then by the second number
    in the player number, etc... player numbers that
    start with a letter are alphabetical at the end
    of the list.
    """
    # In development
    rosterplayers = db.session.query(Player.number, Player.name,
        Player.player_id).join(RosterPlayer).filter(
        RosterPlayer.roster_id == roster_id)
        

    if ordered_by == 'alpha':
        rosterplayers = rosterplayers.order_by(Player.name)
    elif ordered_by == 'num':
        rosterplayers = rosterplayers.order_by(Player.number)
    elif ordered_by == 'derby':
        derby_order = []
        # for player in rosterplayers:


    return redirect("/")


@app.route('/start_jam')
def start_jam():
    """
    Set up the starting jam of each period.
    This does not have the countdown clock of the between_jams.
    """
    # In development

    session['jam_num'] = 1
    session['period_num'] = 1


    return render_template("/html/start_jam.html")


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

@app.route('/clear_session')
def clear_session():
    session.clear()
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