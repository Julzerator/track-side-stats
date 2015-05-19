"""Models and database functions for Track Side Stats project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class User(db.Model):
    """A User of the Track Side Stats that enters the data."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(50), nullable=True)
    lname = db.Column(db.String(50), nullable=True)
    uname = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'),
                        nullable=True)

    team = db.relationship('Team', backref=db.backref('teams'))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User id=%s name=%s email=%s>" % (self.user_id, 
                                                 self.name, self.email)


class LeagueUser(db.Model):
    """A joiner table between User and League."""

    __tablename__ = "leagueusers"
    
    leause_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('leagues.league_id'), nullable=False)
    permission_lvl = db.Column(db.String(50), nullable=True)

    user = db.relationship('User', backref=db.backref('users'))
    league_name = db.relationship('League', backref=db.backref('leagues'))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<LeagueUser id=%s permission_lvl=%s>" % (self.leause_id, self.permission_lvl)


class Team(db.Model):
    """The Team class."""

    __tablename__ = "teams"

    team_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    t_type = db.Column(db.String(100), nullable=False)
    founded = db.Column(db.Date, nullable=False)
    disbanded = db.Column(db.Date, nullable=True)
    league_id = db.Column(db.Integer, db.ForeignKey('leagues.league_id'), nullable=True)
    
    league_name = db.relationship('League', backref=db.backref('leagues'))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Team id=%s name=%s t_type=%s>" % (self.team_id, 
            self.name, self.t_type)


class Player(db.Model):
    """The Player class."""

    __tablename__ = "players"

    player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    legal_fname = db.Column(db.String(50), nullable=True)
    legal_lname = db.Column(db.String(50), nullable=True)
    number = db.Column(db.String(4), nullable=False)
    started = db.Column(db.Date, nullable=False)
    retired = db.Column(db.Date, nullable=True)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Player id=%s name=%s>" % (self.player_id, self.name)


class Position(db.Model):
    """The Position class."""

    __tablename__ = "positions"

    position_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position_type = db.Column(db.String(50), nullable=False)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Position id=%s name=%s type=%s>" % (self.position_id, self.name, 
            self.position_type)


class TeamPlayer(db.Model):
    """A joiner table between Player and Team."""

    __tablename__ = "teamplayers"
    
    teapla_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=True)

    team_name = db.relationship('Team', backref=db.backref('teams'))
    player_name = db.relationship('Player', backref=db.backref('players'))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<TeamPlayer id=%s team_name=%s player_name=%s>" % (self.teapla_id, 
            self.team_name, self.player_name)


class League(db.Model):
    """The League class."""

    __tablename__ = "leagues"

    league_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    affiliation = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Date, nullable=False)
    disbanded = db.Column(db.Date, nullable=True)
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<League id=%s name=%s>" % (self.league_id, self.name)


class Roster(db.Model):
    """The Roster class."""

    __tablename__ = "rosters"

    roster_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    ord = db.Column(db.Integer, nullable=False)
    color = db.Column(db.Integer, nullable=False)

    team_name = db.relationship('Team', backref=db.backref('teams'))
    game_info = db.relationship('Game', backref=db.backref('games'))
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Roster id=%s teamname=%s color=%s>" % (self.roster_id, 
            self.team_name, self.color)


class RosterPlayer(db.Model):
    """A joiner table between Roster and Player."""

    __tablename__ = "rosterplayers"
    
    rospla_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    roster_id = db.Column(db.Integer, db.ForeignKey('rosters.roster_id'), nullable=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=True)

    roster_info = db.relationship('Roster', backref=db.backref('rosters'))
    player_name = db.relationship('Player', backref=db.backref('players'))
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<RosterPlayer id=%s player_name=%s roster_id=%s >" % (self.rospla_id, 
            self.player_name, self.roster_id)


class Game(db.Model):
    """The Game class."""

    __tablename__ = "games"

    game_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    event_name = db.Column(db.String(100), nullable=True)
    g_type = db.Column(db.String(100), nullable=False)
    floor = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Game id=%s date=%s, location=%s>" % (self.game_id, 
            self.date, self.location)


class Jam(db.Model):
    """The Jam class."""

    __tablename__ = "jams"

    jam_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    period = db.Column(db.Integer, nullable=False)
    j_start = db.Column(db.DateTime, nullable=True)
    j_end = db.Column(db.DateTime, nullable=True)
    number = db.Column(db.Integer, nullable=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    timeout_type = db.Column(db.String(25), nullable=True)
    t_start = db.Column(db.DateTime, nullable=True)
    t_end = db.Column(db.DateTime, nullable=True)

    game_info = db.relationship('Game', backref=db.backref('games'))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Jam id=%s period=%s, number=%s>" % (self.jam_id, 
            self.period, self.number)    


class JamPosition(db.Model):
    """A joiner table between Player, Jam, and Position."""

    __tablename__ = "jampositions"
    
    jampos_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    jam_id = db.Column(db.Integer, db.ForeignKey('jams.jam_id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('positions.position_id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)

    jam_info = db.relationship('Jam', backref=db.backref('jams'))
    position_name = db.relationship('Position', backref=db.backref('positions'))
    player_name = db.relationship('Player', backref=db.backref('players'))
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<JamPosition id=%s player_name=%s position_name=%s jam_info=%s>" % (
            self.jampos_id, self.player_name, self.position_name, self.jam_info)


class Action(db.Model):
    """The Action class."""

    __tablename__ = "actions"

    action_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    jam_id = db.Column(db.Integer, db.ForeignKey('jams.jam_id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
    play = db.Column(db.String(20), nullable=False)
    points = db.Column(db.Integer, nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False)

    jam_info = db.relationship('Jam', backref=db.backref('jams'))
    player_name = db.relationship('Player', backref=db.backref('players'))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Action id=%s player_name=%s, play=%s>" % (self.action_id, 
            self.player_name, self.number)    


# End Part 1
##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/trackstats'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."